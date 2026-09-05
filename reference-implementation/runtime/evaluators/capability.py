from runtime.safety_kernel.types import GateResult, PASS, FAIL, PENDING

def evaluate_capability(facts):
    if facts.get("capability_determined") is False:
        return GateResult("CapabilityGate",PENDING,"CAPABILITY_UNDETERMINED")
    if not facts.get("capability_present",False):
        return GateResult("CapabilityGate",FAIL,"CAPABILITY_MISSING")
    return GateResult("CapabilityGate",PASS,"CAPABILITY_PRESENT")
