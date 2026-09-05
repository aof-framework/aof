import json
from pathlib import Path
import pytest
from engine.assurance import evaluate

ROOT=Path(__file__).resolve().parents[2]
FILES=sorted((ROOT/"fixtures/assurance").glob("ECT-ASR-*.json"))

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_positive(path):
    case=json.loads(path.read_text())
    assert evaluate(case).result=="Pass"

MUT={
"ECT-ASR-001":{"claim_treated_as_evidence":True},
"ECT-ASR-002":{"verified_without_evaluation":True},
"ECT-ASR-003":{"criteria_coverage_complete":True},
"ECT-ASR-004":{"provenance_sufficient":False},
"ECT-ASR-005":{"age":5},
"ECT-ASR-006":{"admissible":True},
"ECT-ASR-007":{"reported_to_verification":False},
"ECT-ASR-008":{"verification_result":"Verified"},
"ECT-ASR-009":{"verification_mode":"IndependentAgent","verifier_independent":True},
"ECT-ASR-010":{"pure_self_reference":False},
"ECT-ASR-011":{"explicit_criteria":True},
"ECT-ASR-012":{"consumed_subject_version":"v2"},
"ECT-ASR-013":{"current_subject_version":"v1"},
"ECT-ASR-014":{"authority_created":True},
"ECT-ASR-015":{"approval_created":True},
"ECT-ASR-016":{"required_verification_satisfied":True},
"ECT-ASR-017":{"required_assurance_satisfied":False},
"ECT-ASR-018":{"required_evidence_present":True},
}

@pytest.mark.parametrize("path",FILES,ids=lambda p:p.stem)
def test_adversarial_mutation_detected(path):
    case=json.loads(path.read_text())
    case["facts"].update(MUT[case["test_id"]])
    assert evaluate(case).result=="Fail"

def test_high_risk_self_check_is_insufficient():
    c=json.loads((ROOT/"fixtures/assurance/ECT-ASR-009.json").read_text())
    assert evaluate(c).observed["independence_satisfied"] is False

def test_subject_version_mismatch_invalidates_consumption():
    c=json.loads((ROOT/"fixtures/assurance/ECT-ASR-012.json").read_text())
    c["facts"]["consumed_subject_version"]="v9"
    assert evaluate(c).result=="Fail"

def test_inconclusive_never_completes():
    c=json.loads((ROOT/"fixtures/assurance/ECT-ASR-008.json").read_text())
    assert evaluate(c).observed["successful_completion"] is False

def test_missing_evidence_never_verified():
    c=json.loads((ROOT/"fixtures/assurance/ECT-ASR-018.json").read_text())
    assert evaluate(c).observed["verified"] is False
