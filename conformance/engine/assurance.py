from dataclasses import dataclass, asdict
from typing import Any, Dict, List

PASS="Pass"; FAIL="Fail"; BLOCKED="Blocked"

@dataclass
class Result:
    test_id: str
    result: str
    observed: Dict[str, Any]
    expected: Dict[str, Any]
    evidence: List[Dict[str, Any]]
    notes: List[str]
    def to_dict(self): return asdict(self)

def evaluate(case: Dict[str, Any]) -> Result:
    tid=case["test_id"]; f=dict(case.get("facts",{})); exp=dict(case.get("expected",{})); o={}
    ev=[{"type":"AssuranceObservation","test_id":tid,"facts":f}]

    if tid=="ECT-ASR-001":  # Claim != Evidence
        o["claim_is_evidence"] = bool(f.get("claim_present") and f.get("claim_treated_as_evidence"))
        o["separation_preserved"] = bool(f.get("claim_present") and not f.get("claim_treated_as_evidence"))

    elif tid=="ECT-ASR-002":  # Evidence != Verification
        o["evidence_implies_verified"] = bool(f.get("evidence_present") and f.get("verified_without_evaluation"))
        o["separation_preserved"] = bool(f.get("evidence_present") and not f.get("verified_without_evaluation"))

    elif tid=="ECT-ASR-003":  # Evidence present != sufficient
        o["sufficient"] = bool(f.get("evidence_present") and f.get("criteria_coverage_complete") and f.get("admissible"))
        o["verified"] = bool(o["sufficient"] and f.get("verifier_eligible"))

    elif tid=="ECT-ASR-004":  # provenance required
        o["admissible"] = bool(f.get("source_identifiable") and f.get("provenance_sufficient") and f.get("integrity_ok"))

    elif tid=="ECT-ASR-005":  # stale evidence
        o["fresh"] = bool(f.get("age",0) <= f.get("freshness_limit",0))
        o["verified"] = bool(o["fresh"] and f.get("other_verification_conditions"))

    elif tid=="ECT-ASR-006":  # inadmissible evidence
        o["verified"] = bool(f.get("admissible") and f.get("sufficient") and f.get("verifier_eligible"))
        o["fail_open"] = bool((not f.get("admissible")) and o["verified"])

    elif tid=="ECT-ASR-007":  # contradiction visible
        o["contradiction_visible"] = bool(f.get("material_contradiction") and f.get("reported_to_verification"))
        o["verified"] = bool(f.get("verification_result")=="Verified")

    elif tid=="ECT-ASR-008":  # Inconclusive != Verified
        o["verified"] = f.get("verification_result")=="Verified"
        o["successful_completion"] = bool(o["verified"] and f.get("other_completion_conditions"))

    elif tid=="ECT-ASR-009":  # SelfCheck != IndependentVerification
        o["independence_satisfied"] = bool(
            not f.get("independence_required") or
            (f.get("verification_mode")!="Self" and f.get("verifier_independent"))
        )
        o["verified_at_required_level"] = bool(o["independence_satisfied"] and f.get("verification_result")=="Verified")

    elif tid=="ECT-ASR-010":  # circular verification
        o["independence_satisfied"] = bool(
            f.get("verifier_independent") and not f.get("pure_self_reference") and not f.get("same_control_domain_dependency")
        )
        o["strong_independence_claim_allowed"] = o["independence_satisfied"]

    elif tid=="ECT-ASR-011":  # verification criteria
        o["verification_valid"] = bool(f.get("explicit_criteria") and f.get("evidence_evaluated"))
        o["verified"] = bool(o["verification_valid"] and f.get("verification_result")=="Verified")

    elif tid=="ECT-ASR-012":  # verification subject binding
        o["binding_valid"] = (
            f.get("verified_subject_id")==f.get("consumed_subject_id")
            and f.get("verified_subject_version")==f.get("consumed_subject_version")
        )
        o["verified_for_consumed_subject"] = bool(o["binding_valid"] and f.get("verification_result")=="Verified")

    elif tid=="ECT-ASR-013":  # material subject change => reverification
        changed = f.get("verified_subject_version") != f.get("current_subject_version")
        o["reverification_required"] = changed
        o["old_verification_reusable"] = not changed

    elif tid=="ECT-ASR-014":  # Verification != Authority
        o["authority_created_by_verification"] = bool(f.get("verification_result")=="Verified" and f.get("authority_created"))
        o["separation_preserved"] = bool(f.get("verification_result")=="Verified" and not f.get("authority_created"))

    elif tid=="ECT-ASR-015":  # Verification != Approval
        o["approval_created_by_verification"] = bool(f.get("verification_result")=="Verified" and f.get("approval_created"))
        o["separation_preserved"] = bool(f.get("verification_result")=="Verified" and not f.get("approval_created"))

    elif tid=="ECT-ASR-016":  # execution success != verified outcome
        o["verified_outcome"] = bool(f.get("execution_success") and f.get("required_verification_satisfied"))
        o["completion_allowed"] = bool(o["verified_outcome"] and f.get("goal_satisfied"))

    elif tid=="ECT-ASR-017":  # completion requires goal + assurance
        o["completion_allowed"] = bool(f.get("goal_satisfied") and f.get("required_verification_satisfied") and f.get("required_assurance_satisfied"))

    elif tid=="ECT-ASR-018":  # missing required evidence
        o["verified"] = bool(f.get("required_evidence_present") and f.get("verification_result")=="Verified")
        o["controlled_non_success"] = not o["verified"]

    else:
        return Result(tid,BLOCKED,o,exp,ev,["Unknown Phase 4 evaluator"])

    ok=all(o.get(k)==v for k,v in exp.items())
    return Result(tid,PASS if ok else FAIL,o,exp,ev,[])
