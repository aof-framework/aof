from adapters.reference_adapter import ReferenceAdapter
from runtime.interfaces.adapter import AdapterObservation

class BrownfieldAdapter(ReferenceAdapter):
    def __init__(self, legacy_runtime, state=None):
        super().__init__(state)
        self.legacy_runtime=legacy_runtime

    def invoke_reasoning(self, agent_ref, task_ref, context_snapshot):
        legacy_output=self.legacy_runtime.reason(task_ref,context_snapshot)
        return AdapterObservation({
            "proposal":{
                "agent_ref":agent_ref,
                "task_ref":task_ref,
                "legacy_output":legacy_output,
                "status":"UntrustedProposal"
            }
        },["trace:brownfield-proposal-produced"])
