import json
from pathlib import Path
import pytest

from runtime.state.store import InMemoryStateStore
from runtime.trace.recorder import InMemoryTraceRecorder
from runtime.e2e.orchestrator import ReferenceOrchestrator
from adapters.e2e_adapters import NativeReferenceAdapter, BrownfieldReferenceAdapter, SyntheticLegacyRuntime

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/e2e").glob("E2E-*.json"))

def adapter_for(mode):
    if mode=="AOFNative":
        return NativeReferenceAdapter()
    return BrownfieldReferenceAdapter(SyntheticLegacyRuntime())

def build(case):
    adapter=adapter_for(case["mode"])
    state=InMemoryStateStore()
    state.put("subject:demo",{"status":"ready"},"1")
    trace=InMemoryTraceRecorder()
    orch=ReferenceOrchestrator(adapter,state,trace)
    return orch,adapter,state,trace

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_e2e_scenario(path):
    c=json.loads(path.read_text())
    orch,adapter,state,trace=build(c)
    prepared=orch.prepare(c["request"],c["initial_facts"])
    contract=orch.issue_execution_contract(c["request"],prepared,f"contract:{c['test_id']}")
    assert contract is not None
    result=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    assert result["status"]==c["expected_effect_status"]

def test_native_and_brownfield_governance_equivalence_happy_path():
    results=[]
    for mode in ("AOFNative","AdapterBasedBrownfield"):
        c=json.loads((ROOT/f"fixtures/e2e/{'E2E-001' if mode=='AOFNative' else 'E2E-002'}.json").read_text())
        orch,adapter,state,trace=build(c)
        p=orch.prepare(c["request"],c["initial_facts"])
        contract=orch.issue_execution_contract(c["request"],p,f"contract:eq:{mode}")
        r=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
        results.append((p["decision"].status,r["status"],r["effect_occurred"]))
    assert results[0]==results[1]==("Allow","Executed",True)

def test_native_and_brownfield_revocation_equivalence():
    statuses=[]
    for fn in ("E2E-003.json","E2E-004.json"):
        c=json.loads((ROOT/"fixtures/e2e"/fn).read_text())
        orch,adapter,state,trace=build(c)
        p=orch.prepare(c["request"],c["initial_facts"])
        contract=orch.issue_execution_contract(c["request"],p,f"contract:{fn}")
        r=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
        statuses.append(r["status"])
        assert adapter.effects==[]
    assert statuses==["Blocked","Blocked"]

def test_brownfield_reasoning_remains_untrusted_proposal():
    c=json.loads((ROOT/"fixtures/e2e/E2E-002.json").read_text())
    orch,adapter,state,trace=build(c)
    p=orch.prepare(c["request"],c["initial_facts"])
    assert p["proposal"]["status"]=="UntrustedProposal"

def test_brownfield_policy_deny_cannot_be_suppressed():
    c=json.loads((ROOT/"fixtures/e2e/E2E-006.json").read_text())
    orch,adapter,state,trace=build(c)
    p=orch.prepare(c["request"],c["initial_facts"])
    contract=orch.issue_execution_contract(c["request"],p,"contract:deny")
    r=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    assert r["status"]=="Blocked"
    assert adapter.effects==[]

def test_state_change_between_decision_and_effect_blocks_both_modes():
    for mode in ("AOFNative","AdapterBasedBrownfield"):
        c=json.loads((ROOT/"fixtures/e2e/E2E-001.json").read_text())
        c["mode"]=mode
        orch,adapter,state,trace=build(c)
        p=orch.prepare(c["request"],c["initial_facts"])
        contract=orch.issue_execution_contract(c["request"],p,f"contract:state:{mode}")
        state.transition("subject:demo","1",{"status":"changed"},"2")
        r=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
        assert r["status"]=="Blocked"
        assert r["reason"]=="STATE_STALE_AT_EFFECT"

def test_replay_rejected_in_brownfield_mode():
    c=json.loads((ROOT/"fixtures/e2e/E2E-002.json").read_text())
    orch,adapter,state,trace=build(c)
    p=orch.prepare(c["request"],c["initial_facts"])
    contract=orch.issue_execution_contract(c["request"],p,"contract:replay")
    first=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    second=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    assert first["status"]=="Executed"
    assert second["status"]=="Blocked"
    assert len(adapter.effects)==1

def test_trace_correlates_decision_contract_and_effect():
    c=json.loads((ROOT/"fixtures/e2e/E2E-002.json").read_text())
    orch,adapter,state,trace=build(c)
    p=orch.prepare(c["request"],c["initial_facts"])
    contract=orch.issue_execution_contract(c["request"],p,"contract:trace")
    orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    types=[e["event_type"] for e in trace.all()]
    assert "GovernanceDecision" in types
    assert "ExecutionContractIssued" in types
    assert "EffectBoundaryRevalidation" in types
    assert "EffectDispatchCompleted" in types

def test_effect_evidence_can_be_verified_but_is_not_verification_itself():
    c=json.loads((ROOT/"fixtures/e2e/E2E-001.json").read_text())
    orch,adapter,state,trace=build(c)
    p=orch.prepare(c["request"],c["initial_facts"])
    contract=orch.issue_execution_contract(c["request"],p,"contract:verify")
    r=orch.execute(contract["id"],{"semantic_effect":"write:demo"},c["effect_facts"])
    assert r["status"]=="Executed"
    evidence=[{
        "id":"evidence:e2e","subject_ref":"subject:demo","subject_version":"1",
        "provenance":{"execution_ref":"contract:verify"},
        "supports_criteria":True
    }]
    v=orch.verify_effect("subject:demo","1",evidence)
    assert v.status=="Verified"
    assert v.evidence_refs==["evidence:e2e"]

def test_conformance_report_bound_to_scope_and_profile():
    c=json.loads((ROOT/"fixtures/e2e/E2E-001.json").read_text())
    orch,adapter,state,trace=build(c)
    report=orch.report_conformance({
        "id":"manifest:e2e","subject":"system:e2e","subject_version":"1",
        "profile":"AOF-Core","scope":{"components":["reference-runtime"]},
        "mandatory_requirement_ids":["REQ-E2E"],
        "requirements":[{"id":"REQ-E2E","test_results":["Pass"],"evidence_required":True,"evidence_refs":["evidence:e2e"]}]
    })
    assert report["final_result"]=="Conformant"
    assert report["profile"]=="AOF-Core"
    assert report["scope"]=={"components":["reference-runtime"]}

def test_partial_scope_does_not_become_full_claim():
    c=json.loads((ROOT/"fixtures/e2e/E2E-001.json").read_text())
    orch,adapter,state,trace=build(c)
    report=orch.report_conformance({
        "id":"manifest:partial","subject":"system:e2e","subject_version":"1",
        "profile":"AOF-Core","scope":{"components":["adapter-only"]},
        "limitations":["only adapter boundary assessed"],
        "mandatory_requirement_ids":["REQ-E2E"],
        "requirements":[{"id":"REQ-E2E","test_results":["Pass"],"evidence_refs":["evidence:e2e"]}]
    })
    assert report["final_result"]=="Conditional"
