from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_verification(facts):
    if facts.get("verification_required") is False:
        return GateResult("VerificationGate",PASS,"VERIFICATION_NOT_REQUIRED")
    status=facts.get("verification_status")
    if status is None:
        return GateResult("VerificationGate",PENDING,"VERIFICATION_MISSING")
    if status=="Inconclusive":
        return GateResult("VerificationGate",PENDING,"VERIFICATION_INCONCLUSIVE")
    if status=="Pending":
        return GateResult("VerificationGate",PENDING,"VERIFICATION_PENDING")
    if status=="Failed":
        return GateResult("VerificationGate",FAIL,"VERIFICATION_FAILED")
    if status!="Verified":
        return GateResult("VerificationGate",PENDING,"VERIFICATION_UNKNOWN")
    if facts.get("verification_stale",False):
        return GateResult("VerificationGate",FAIL,"VERIFICATION_STALE")
    return GateResult("VerificationGate",PASS,"VERIFICATION_VERIFIED")
