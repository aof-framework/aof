TEST_RESULTS={"Pass","Fail","Blocked","NotApplicable","Inconclusive"}

def aggregate_requirement(requirement):
    applicability=requirement.get("applicability","Applicable")
    if applicability=="NotApplicable":
        if not requirement.get("applicability_rationale"):
            return "Inconclusive"
        if requirement.get("required_by_claimed_scope") is True:
            return "Inconclusive"
        return "NotApplicable"

    tests=requirement.get("test_results",[])
    if not tests:
        return "Inconclusive"
    if any(t not in TEST_RESULTS for t in tests):
        return "Inconclusive"
    if "Fail" in tests:
        return "Violated"
    if "Blocked" in tests or "Inconclusive" in tests:
        return "Inconclusive"

    has_pass="Pass" in tests
    if not has_pass:
        return "Inconclusive"

    if requirement.get("evidence_required",False) and not requirement.get("evidence_refs"):
        return "Inconclusive"
    return "Satisfied"

def aggregate_conformance(claim):
    for field in ("subject","subject_version","profile","scope"):
        if not claim.get(field):
            return "Inconclusive"

    reqs=claim.get("requirements",[])
    mandatory_ids=set(claim.get("mandatory_requirement_ids",[]))
    observed_ids={r.get("id") for r in reqs}

    if mandatory_ids - observed_ids:
        return "Inconclusive"

    normalized=[]
    for r in reqs:
        rr=dict(r)
        rr["requirement_result"]=rr.get("requirement_result") or aggregate_requirement(rr)
        normalized.append(rr)

    for r in normalized:
        if r.get("id") in mandatory_ids and r["requirement_result"]=="Violated":
            return "NonConformant"

    for r in normalized:
        if r.get("id") in mandatory_ids and r["requirement_result"]=="Inconclusive":
            return "Inconclusive"

    if any(r["requirement_result"]=="Violated" for r in normalized):
        return "NonConformant"
    if any(r["requirement_result"]=="Inconclusive" for r in normalized):
        return "Inconclusive"

    if claim.get("conditional_applicability") or claim.get("exceptions") or claim.get("limitations"):
        return "Conditional"

    return "Conformant"
