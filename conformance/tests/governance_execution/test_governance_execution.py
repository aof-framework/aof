import json
from pathlib import Path
import pytest
from engine.governance_execution import evaluate
ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/governance_execution").glob("ECT-GEX-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_positive(path):
    c=json.loads(path.read_text())
    assert evaluate(c).result=="Pass"

MUT={
"ECT-GEX-001":{"child_operations":["read","delete"]},
"ECT-GEX-002":{"grant_at_effect":{"status":"Active"}},
"ECT-GEX-003":{"effect_time":5},
"ECT-GEX-004":{"policy_effects":["Allow"]},
"ECT-GEX-005":{"mandatory_policy_result":"Allow"},
"ECT-GEX-006":{"action_risk":2},
"ECT-GEX-007":{"execution_contract_valid":True},
"ECT-GEX-008":{"already_consumed":False},
"ECT-GEX-009":{"current_state_version":7},
"ECT-GEX-010":{"transition_authorized":True},
"ECT-GEX-011":{"attempt":2},
"ECT-GEX-012":{"retry_operations":["read","write"]},
"ECT-GEX-013":{"resource_scope_changed":False},
"ECT-GEX-014":{"effect_boundary_revalidated":True},
"ECT-GEX-015":{"authority_created":True},
"ECT-GEX-016":{"effect_trace":False}}
@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_adversarial_mutation_detected(path):
    c=json.loads(path.read_text()); c["facts"].update(MUT[c["test_id"]])
    assert evaluate(c).result=="Fail"

def test_delegation_resource_expansion_detected():
    c=json.loads((ROOT/"fixtures/governance_execution/ECT-GEX-001.json").read_text())
    c["facts"]["child_resources"]=["repo","prod"]; assert evaluate(c).result=="Fail"

def test_delegation_risk_expansion_detected():
    c=json.loads((ROOT/"fixtures/governance_execution/ECT-GEX-001.json").read_text())
    c["facts"]["child_risk_ceiling"]=4; assert evaluate(c).result=="Fail"

def test_revoked_status_never_active_at_effect():
    c=json.loads((ROOT/"fixtures/governance_execution/ECT-GEX-002.json").read_text())
    assert evaluate(c).observed["valid_at_effect"] is False
