from runtime.safety_kernel.types import SafetyKernelDecision, PASS, FAIL, PENDING
from runtime.evaluators.capability import evaluate_capability
from runtime.evaluators.authority import evaluate_authority
from runtime.evaluators.policy import evaluate_policy
from runtime.evaluators.state import evaluate_state
from runtime.evaluators.risk import evaluate_risk
from runtime.evaluators.verification import evaluate_verification

class SafetyKernel:
    """Reference Safety Kernel for AOF v1.0.

    Hard rule:
      ExecuteAllowed = C and H and P and S and R and V

    Any Fail -> Deny.
    No Fail but at least one Pending -> Pending.
    Only all Pass -> Allow.
    """

    def evaluate(self, facts):
        gates = {
            "capability": evaluate_capability(facts),
            "authority": evaluate_authority(facts),
            "policy": evaluate_policy(facts),
            "state": evaluate_state(facts),
            "risk": evaluate_risk(facts),
            "verification": evaluate_verification(facts),
        }

        statuses=[g.status for g in gates.values()]
        reasons=[g.reason_code for g in gates.values() if g.status != PASS]

        if FAIL in statuses:
            return SafetyKernelDecision(
                status="Deny",
                execute_allowed=False,
                gate_results=gates,
                reason_codes=reasons
            )
        if PENDING in statuses:
            return SafetyKernelDecision(
                status="Pending",
                execute_allowed=False,
                gate_results=gates,
                reason_codes=reasons
            )
        return SafetyKernelDecision(
            status="Allow",
            execute_allowed=True,
            gate_results=gates,
            reason_codes=[]
        )
