from dataclasses import dataclass, asdict
from typing import Any, Dict, List

APPLICABLE = {"Applicable","NotApplicable","Conditional"}
TEST_RESULTS = {"Pass","Fail","Blocked","NotApplicable","Inconclusive"}
REQ_RESULTS = {"Satisfied","Violated","NotApplicable","Inconclusive"}
CONF_RESULTS = {"Conformant","NonConformant","Conditional","Inconclusive"}

@dataclass
class RequirementEvaluation:
    requirement_id: str
    applicability: str
    result: str
    test_refs: List[str]
    evidence_refs: List[str]
    limitations: List[str]

@dataclass
class ConformanceEvaluation:
    final_result: str
    requirement_evaluations: List[RequirementEvaluation]
    notes: List[str]

    def to_dict(self):
        return {
            "final_result": self.final_result,
            "requirement_evaluations": [asdict(x) for x in self.requirement_evaluations],
            "notes": self.notes,
        }

def aggregate_requirement(req: Dict[str, Any]) -> RequirementEvaluation:
    rid = req["requirement_id"]
    applicability = req["applicability"]
    tests = req.get("tests", [])
    evidence_refs = req.get("evidence_refs", [])
    limitations = list(req.get("limitations", []))
    mandatory = req.get("normative_level") in ("MUST","MUST NOT")

    if applicability == "NotApplicable":
        return RequirementEvaluation(rid, applicability, "NotApplicable",
                                     [t["test_id"] for t in tests], evidence_refs, limitations)

    if not tests:
        return RequirementEvaluation(rid, applicability, "Inconclusive", [], evidence_refs,
                                     limitations + ["No executable test result supplied."])

    results = [t["result"] for t in tests]

    if any(r == "Fail" for r in results):
        result = "Violated"
    elif any(r in ("Blocked","Inconclusive") for r in results):
        result = "Inconclusive"
    elif all(r in ("Pass","NotApplicable") for r in results):
        # Applicable requirement cannot be satisfied solely by NotApplicable tests.
        if all(r == "NotApplicable" for r in results):
            result = "Inconclusive"
        else:
            result = "Satisfied"
    else:
        result = "Inconclusive"

    # Missing evidence for a requirement that explicitly requires evidence
    # prevents unconditional satisfaction.
    if req.get("evidence_required") and not evidence_refs and result == "Satisfied":
        result = "Inconclusive"
        limitations.append("Required evidence not bound.")

    # The mandatory flag does not alter requirement result vocabulary;
    # it affects final conformance propagation.
    _ = mandatory
    return RequirementEvaluation(rid, applicability, result,
                                 [t["test_id"] for t in tests], evidence_refs, limitations)

def aggregate_conformance(claim: Dict[str, Any]) -> ConformanceEvaluation:
    notes=[]
    reqs=[aggregate_requirement(r) for r in claim.get("requirements",[])]

    # Scope/profile/evidence binding is part of claim validity.
    if not claim.get("subject") or not claim.get("subject_version"):
        return ConformanceEvaluation("Inconclusive", reqs, ["Subject/version binding missing."])
    if not claim.get("profile"):
        return ConformanceEvaluation("Inconclusive", reqs, ["Profile binding missing."])
    if not claim.get("scope"):
        return ConformanceEvaluation("Inconclusive", reqs, ["Scope binding missing."])

    mandatory_ids=set(claim.get("mandatory_requirement_ids",[]))
    by_id={r.requirement_id:r for r in reqs}

    # A failed applicable mandatory MUST/MUST NOT prevents unconditional Conformant.
    if any(by_id[rid].applicability!="NotApplicable" and by_id[rid].result=="Violated"
           for rid in mandatory_ids if rid in by_id):
        return ConformanceEvaluation("NonConformant", reqs, notes)

    # Mandatory requirements that are missing from assessment also prevent Conformant.
    missing_mandatory=[rid for rid in mandatory_ids if rid not in by_id]
    if missing_mandatory:
        notes.append("Mandatory requirements absent from assessment: "+",".join(sorted(missing_mandatory)))
        return ConformanceEvaluation("Inconclusive", reqs, notes)

    # An applicable mandatory requirement cannot be Inconclusive for unconditional conformance.
    if any(by_id[rid].applicability!="NotApplicable" and by_id[rid].result=="Inconclusive"
           for rid in mandatory_ids if rid in by_id):
        return ConformanceEvaluation("Inconclusive", reqs, notes)

    # Any non-mandatory applicable violation prevents unconditional Conformant too;
    # use Conditional only when limitations/conditional applicability are explicit
    # and no applicable requirement is Violated.
    if any(r.applicability!="NotApplicable" and r.result=="Violated" for r in reqs):
        return ConformanceEvaluation("NonConformant", reqs, notes)

    if any(r.applicability!="NotApplicable" and r.result=="Inconclusive" for r in reqs):
        return ConformanceEvaluation("Inconclusive", reqs, notes)

    conditional = (
        any(r.applicability=="Conditional" for r in reqs)
        or bool(claim.get("exceptions"))
        or bool(claim.get("limitations"))
    )
    if conditional:
        return ConformanceEvaluation("Conditional", reqs, notes)

    return ConformanceEvaluation("Conformant", reqs, notes)

def validate_not_applicable(req: Dict[str, Any]) -> bool:
    if req.get("applicability")!="NotApplicable":
        return True
    # Anti-loophole: N/A must have rationale, and cannot be used when explicitly required by profile/scope.
    if not req.get("applicability_rationale"):
        return False
    if req.get("required_by_claimed_scope"):
        return False
    return True
