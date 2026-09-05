import json
from pathlib import Path
import pytest
from engine.core_semantics import evaluate

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / "fixtures" / "core"

CASE_FILES = sorted(FIX.glob("ECT-CORE-*.json"))

@pytest.mark.parametrize("path", CASE_FILES, ids=lambda p: p.stem)
def test_positive_core_semantics(path):
    case = json.loads(path.read_text(encoding="utf-8"))
    result = evaluate(case)
    assert result.result == "Pass", result.to_dict()

MUTATIONS = {
    "ECT-CORE-001": {"authority": False, "execute_allowed_override": True}, # custom below
    "ECT-CORE-002": {"decision_authorized": True},
    "ECT-CORE-003": {"authority_from_agent_output": True},
    "ECT-CORE-004": {"approval": True, "pending": False},
    "ECT-CORE-005": {"execute": True},
    "ECT-CORE-006": {"policy_changed": True},
    "ECT-CORE-007": {"execute": True},
    "ECT-CORE-008": {"authority_created": True},
    "ECT-CORE-009": {"execute": True},
    "ECT-CORE-010": {"safety_kernel_evaluated": False},
    "ECT-CORE-011": {"execute": True},
    "ECT-CORE-012": {"governance_root": True},
}

@pytest.mark.parametrize("path", CASE_FILES, ids=lambda p: p.stem)
def test_negative_core_semantics_are_detected(path):
    case = json.loads(path.read_text(encoding="utf-8"))
    tid = case["test_id"]
    mutation = dict(MUTATIONS[tid])
    mutation.pop("execute_allowed_override", None)
    case["facts"].update(mutation)

    # ECT-CORE-001 negative means falsely granting Authority based on Capability.
    if tid == "ECT-CORE-001":
        case["facts"]["authority"] = True
        case["expected"]["authority_created_by_capability"] = False
        case["expected"]["execute_allowed"] = False

    result = evaluate(case)
    assert result.result == "Fail", result.to_dict()

def test_no_implicit_permit_on_missing_safety_predicate():
    from engine.core_semantics import execute_allowed
    assert execute_allowed({
        "capability": True,
        "authority": True,
        "policy": True,
        "state": True,
        "risk": True,
        # verification intentionally missing
    }) is False

def test_all_explicit_safety_predicates_required():
    from engine.core_semantics import execute_allowed
    assert execute_allowed({
        "capability": True,
        "authority": True,
        "policy": True,
        "state": True,
        "risk": True,
        "verification": True,
    }) is True
