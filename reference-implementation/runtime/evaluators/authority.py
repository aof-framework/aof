from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_authority(facts):
    if facts.get("authority_determined") is False:
        return GateResult("AuthorityEvaluator",PENDING,"AUTHORITY_UNDETERMINED")
    if not facts.get("authority_granted",False):
        return GateResult("AuthorityEvaluator",FAIL,"NO_AUTHORITY_GRANT")
    if facts.get("authority_revoked",False):
        return GateResult("AuthorityEvaluator",FAIL,"AUTHORITY_REVOKED")
    if facts.get("authority_expired",False):
        return GateResult("AuthorityEvaluator",FAIL,"AUTHORITY_EXPIRED")
    if facts.get("scope_match") is False:
        return GateResult("AuthorityEvaluator",FAIL,"AUTHORITY_SCOPE_MISMATCH")
    return GateResult("AuthorityEvaluator",PASS,"AUTHORITY_VALID")
