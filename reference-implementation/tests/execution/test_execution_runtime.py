import json
from pathlib import Path
import pytest

from runtime.state.store import InMemoryStateStore
from runtime.trace.recorder import InMemoryTraceRecorder
from runtime.execution.contracts import ExecutionContractRegistry
from runtime.execution.runtime import ExecutionRuntime
from adapters.test_effect_adapter import SyntheticEffectAdapter

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/execution").glob("EXE-*.json"))

def build(case, adapter_mode="execute"):
    store=InMemoryStateStore()
    s=case["state"]
    store.put(s["subject_ref"],s["state"],s["version"])
    trace=InMemoryTraceRecorder()
    reg=ExecutionContractRegistry()
    reg.register(case["contract"])
    adapter=SyntheticEffectAdapter(mode=adapter_mode)
    rt=ExecutionRuntime(adapter,store,trace,reg)
    return rt,store,trace,reg,adapter

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_fixture(path):
    case=json.loads(path.read_text())
    rt,store,trace,reg,adapter=build(case)
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]==case["expected_status"]

def test_single_use_replay_rejected():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    first=rt.execute(case["contract"]["id"],{"op":"one"},case["facts"])
    second=rt.execute(case["contract"]["id"],{"op":"two"},case["facts"])
    assert first["status"]=="Executed"
    assert second["status"]=="Blocked"
    assert second["reason"]=="EXECUTION_CONTRACT_REPLAY"
    assert len(adapter.effects)==1

def test_state_change_after_decision_blocks_effect():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    store.transition("subject:1","1",{"status":"changed"},"2")
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]=="Blocked"
    assert r["reason"]=="STATE_STALE_AT_EFFECT"
    assert adapter.effects==[]

def test_revocation_after_prior_allow_blocks_effect():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    facts=dict(case["facts"])
    facts["authority_revoked"]=True
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},facts)
    assert r["status"]=="Blocked"
    assert r["effect_occurred"] is False

def test_policy_change_after_prior_allow_blocks_effect():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    facts=dict(case["facts"])
    facts["explicit_deny"]=True
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},facts)
    assert r["status"]=="Blocked"
    assert adapter.effects==[]

def test_unknown_effect_never_reported_success():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case,"unknown")
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]=="UnknownEffect"
    assert r["effect_occurred"] is None

def test_adapter_failure_traced_and_not_success():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case,"raise")
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]=="Failed"
    assert r["effect_occurred"] is False
    assert any(e["event_type"]=="EffectDispatchFailed" for e in trace.all())

def test_success_trace_has_revalidation_and_dispatch():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    events=[e["event_type"] for e in trace.find_by_execution(case["contract"]["id"])]
    assert r["status"]=="Executed"
    assert "EffectBoundaryRevalidation" in events
    assert "EffectDispatchStarted" in events
    assert "EffectDispatchCompleted" in events

def test_blocked_effect_has_no_dispatch_started():
    case=json.loads((ROOT/"fixtures/execution/EXE-003.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    events=[e["event_type"] for e in trace.find_by_execution(case["contract"]["id"])]
    assert r["status"]=="Blocked"
    assert "EffectDispatchStarted" not in events

def test_contract_itself_does_not_create_authority():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    case["facts"]["authority_granted"]=False
    rt,store,trace,reg,adapter=build(case)
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]=="Blocked"
    assert adapter.effects==[]

def test_missing_contract_fails_closed():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    r=rt.execute("contract:missing",{"op":"synthetic"},case["facts"])
    assert r["status"]=="Blocked"
    assert r["reason"]=="EXECUTION_CONTRACT_NOT_FOUND"

def test_missing_state_fails_closed():
    case=json.loads((ROOT/"fixtures/execution/EXE-001.json").read_text())
    rt,store,trace,reg,adapter=build(case)
    store._states.clear()
    r=rt.execute(case["contract"]["id"],{"op":"synthetic"},case["facts"])
    assert r["status"]=="Blocked"
    assert r["reason"]=="STATE_NOT_FOUND"
