from dataclasses import dataclass, field
from typing import List, Dict
from runtime.assurance.evidence import evidence_is_admissible

@dataclass
class VerificationResult:
    status: str  # Verified | Failed | Inconclusive | NotApplicable
    subject_ref: str
    subject_version: str
    criteria_ref: str
    evidence_refs: List[str] = field(default_factory=list)
    reason_codes: List[str] = field(default_factory=list)
    verifier_ref: str = ""
    independent: bool = False

class VerificationEngine:
    def verify(self, subject_ref, subject_version, criteria_ref, evidence_items,
               verifier_ref, subject_actor_ref=None, independence_required=False):
        if not criteria_ref:
            return VerificationResult(
                "Inconclusive", subject_ref, str(subject_version), "",
                [], ["VERIFICATION_CRITERIA_MISSING"], verifier_ref, False
            )

        independent = subject_actor_ref is None or verifier_ref != subject_actor_ref
        if independence_required and not independent:
            return VerificationResult(
                "Inconclusive", subject_ref, str(subject_version), criteria_ref,
                [], ["VERIFICATION_INDEPENDENCE_NOT_SATISFIED"], verifier_ref, False
            )

        if not evidence_items:
            return VerificationResult(
                "Inconclusive", subject_ref, str(subject_version), criteria_ref,
                [], ["REQUIRED_EVIDENCE_MISSING"], verifier_ref, independent
            )

        admissible=[]
        reasons=[]
        for e in evidence_items:
            ok, reason=evidence_is_admissible(e, subject_ref, subject_version)
            if ok:
                admissible.append(e)
            else:
                reasons.append(reason)

        if not admissible:
            return VerificationResult(
                "Inconclusive", subject_ref, str(subject_version), criteria_ref,
                [], reasons or ["NO_ADMISSIBLE_EVIDENCE"], verifier_ref, independent
            )

        if any(e.get("contradicts_claim") is True for e in admissible):
            return VerificationResult(
                "Failed", subject_ref, str(subject_version), criteria_ref,
                [e["id"] for e in admissible],
                ["MATERIAL_CONTRADICTION"], verifier_ref, independent
            )

        if any(e.get("supports_criteria") is not True for e in admissible):
            return VerificationResult(
                "Inconclusive", subject_ref, str(subject_version), criteria_ref,
                [e["id"] for e in admissible],
                ["EVIDENCE_INSUFFICIENT"], verifier_ref, independent
            )

        return VerificationResult(
            "Verified", subject_ref, str(subject_version), criteria_ref,
            [e["id"] for e in admissible],
            [], verifier_ref, independent
        )
