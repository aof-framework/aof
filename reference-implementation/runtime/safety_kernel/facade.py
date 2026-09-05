from runtime.safety_kernel.kernel import SafetyKernel

class GovernedRuntimeFacade:
    """RI-2 facade: evaluates governance; does not execute consequential effects."""

    def __init__(self, adapter, kernel=None):
        self.adapter=adapter
        self.kernel=kernel or SafetyKernel()

    def evaluate_request(self, proposal, subject_state):
        observed=self.adapter.resolve_governance_inputs(proposal,subject_state)
        facts=dict(observed.payload.get("facts", observed.payload))
        decision=self.kernel.evaluate(facts)
        return {
            "decision":decision,
            "trace_refs":observed.trace_refs,
            "evidence_refs":observed.evidence_refs,
        }

    def execute_effect(self, *args, **kwargs):
        raise NotImplementedError(
            "RI-2 does not execute consequential effects. "
            "RI-3 will integrate Effect Boundary execution."
        )
