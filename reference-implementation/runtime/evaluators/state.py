from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_state(facts):
    if facts.get("state_determined") is False:
        return GateResult("StateValidator",PENDING,"STATE_UNDETERMINED")
    if facts.get("state_stale",False):
        return GateResult("StateValidator",FAIL,"STATE_STALE")
    if facts.get("state_transition_authorized") is False:
        return GateResult("StateValidator",FAIL,"STATE_TRANSITION_UNAUTHORIZED")
    if not facts.get("state_valid",False):
        return GateResult("StateValidator",FAIL,"STATE_INVALID")
    return GateResult("StateValidator",PASS,"STATE_VALID")
