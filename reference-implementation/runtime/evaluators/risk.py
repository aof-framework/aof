from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_risk(facts):
    if facts.get("risk_determined") is False:
        return GateResult("RiskGate",PENDING,"RISK_UNDETERMINED")
    if facts.get("risk_ceiling_exceeded",False):
        return GateResult("RiskGate",FAIL,"RISK_CEILING_EXCEEDED")
    if facts.get("risk_acceptance_required",False) and not facts.get("risk_accepted",False):
        return GateResult("RiskGate",FAIL,"RISK_NOT_ACCEPTED")
    if not facts.get("risk_permits",False):
        return GateResult("RiskGate",FAIL,"RISK_NOT_PERMITTED")
    return GateResult("RiskGate",PASS,"RISK_PERMITS")
