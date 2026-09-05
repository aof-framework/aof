import json
from pathlib import Path
import pytest
from engine.adoption import evaluate

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/adoption").glob("ECT-ADP-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_positive(path):
    c=json.loads(path.read_text())
    assert evaluate(c).result=="Pass"

MUT={
"ECT-ADP-001":{"canonical_controls_present":False},
"ECT-ADP-002":{"mandatory_controls_enforced":False},
"ECT-ADP-003":{"common_governance_boundary":False},
"ECT-ADP-004":{"selected_boundary_governed":False},
"ECT-ADP-005":{"profile":None},
"ECT-ADP-006":{"excluded_mandatory_applicable_control":True},
"ECT-ADP-007":{"authority_semantics_preserved":False},
"ECT-ADP-008":{"authority_expanded":True},
"ECT-ADP-009":{"deny_propagated":False},
"ECT-ADP-010":{"requires_http_or_rest":True},
"ECT-ADP-011":{"requires_replacing_unrelated_tooling":True},
"ECT-ADP-012":{"claim_scope":3},
"ECT-ADP-013":{"claim_limited_to_current_stage":False},
"ECT-ADP-014":{"claims_full_compliance":True},
"ECT-ADP-015":{"effect_observable":False},
"ECT-ADP-016":{"hidden_fields_change_governance_outcome":True},
"ECT-ADP-017":{"adapter_decision":"Allow"},
"ECT-ADP-018":{"effect_occurs":True},
"ECT-ADP-019":{"legacy_event_correlated":False},
"ECT-ADP-020":{"scope":None},
}

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_adversarial_mutation_detected(path):
    c=json.loads(path.read_text())
    c["facts"].update(MUT[c["test_id"]])
    assert evaluate(c).result=="Fail"

def test_brownfield_adapter_does_not_require_big_bang_replacement():
    c=json.loads((ROOT/"fixtures/adoption/ECT-ADP-002.json").read_text())
    r=evaluate(c)
    assert r.observed["replacement_required"] is False

def test_scope_anti_loophole():
    c=json.loads((ROOT/"fixtures/adoption/ECT-ADP-006.json").read_text())
    c["facts"]["excluded_mandatory_applicable_control"]=True
    assert evaluate(c).observed["claim_valid"] is False

def test_transport_agnostic():
    c=json.loads((ROOT/"fixtures/adoption/ECT-ADP-010.json").read_text())
    assert evaluate(c).observed["valid"] is True

def test_partial_adoption_not_full_compliance():
    c=json.loads((ROOT/"fixtures/adoption/ECT-ADP-014.json").read_text())
    c["facts"]["claims_full_compliance"]=True
    assert evaluate(c).observed["valid"] is False

def test_revocation_enforced_through_adapter():
    c=json.loads((ROOT/"fixtures/adoption/ECT-ADP-018.json").read_text())
    assert evaluate(c).observed["revocation_enforced"] is True
