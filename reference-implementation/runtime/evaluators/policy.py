from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_policy(facts):
    if facts.get("policy_determined") is False:
        return GateResult("PolicyEvaluator",PENDING,"POLICY_UNDETERMINED")
    if facts.get("explicit_deny",False):
        return GateResult("PolicyEvaluator",FAIL,"POLICY_DENY")
    if facts.get("mandatory_policy_unknown",False):
        return GateResult("PolicyEvaluator",PENDING,"MANDATORY_POLICY_UNKNOWN")
    if not facts.get("policy_permits",False):
        return GateResult("PolicyEvaluator",FAIL,"POLICY_NOT_PERMITTED")
    return GateResult("PolicyEvaluator",PASS,"POLICY_PERMITS")
