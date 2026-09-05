from adapters.reference_adapter import ReferenceAdapter
from runtime.interfaces.adapter import AdapterObservation, EffectExecutionResult

class NativeReferenceAdapter(ReferenceAdapter):
    mode="AOFNative"
    def __init__(self):
        super().__init__()
        self.effects=[]

    def execute_effect(self, execution_contract, effect_request):
        self.effects.append(effect_request)
        return EffectExecutionResult(
            status="Executed",
            payload={"semantic_effect":effect_request["semantic_effect"]},
            trace_refs=["trace:native-effect"],
            evidence_refs=["evidence:native-effect"],
            effect_known=True
        )

class BrownfieldReferenceAdapter(ReferenceAdapter):
    mode="AdapterBasedBrownfield"
    def __init__(self, legacy_runtime):
        super().__init__()
        self.legacy_runtime=legacy_runtime
        self.effects=[]

    def invoke_reasoning(self, agent_ref, task_ref, context_snapshot):
        raw=self.legacy_runtime.reason(task_ref,context_snapshot)
        return AdapterObservation(
            payload={"proposal":{
                "agent_ref":agent_ref,"task_ref":task_ref,
                "legacy_output":raw,"status":"UntrustedProposal"
            }},
            trace_refs=["trace:brownfield-reasoning"]
        )

    def execute_effect(self, execution_contract, effect_request):
        raw=self.legacy_runtime.execute(effect_request)
        self.effects.append(effect_request)
        return EffectExecutionResult(
            status="Executed",
            payload={"semantic_effect":effect_request["semantic_effect"],"legacy_result":raw},
            trace_refs=["trace:brownfield-effect"],
            evidence_refs=["evidence:brownfield-effect"],
            effect_known=True
        )

class SyntheticLegacyRuntime:
    def reason(self, task_ref, context):
        return {"legacy_proposal_for":task_ref}
    def execute(self, effect_request):
        return {"legacy_status":"ok","semantic_effect":effect_request["semantic_effect"]}
