from runtime.interfaces.adapter import EffectExecutionResult
from adapters.reference_adapter import ReferenceAdapter

class SyntheticEffectAdapter(ReferenceAdapter):
    def __init__(self, mode="execute", state=None):
        super().__init__(state=state)
        self.mode = mode
        self.effects = []

    def execute_effect(self, execution_contract, effect_request):
        if self.mode == "raise":
            raise RuntimeError("synthetic adapter failure")
        if self.mode == "unknown":
            return EffectExecutionResult(
                status="UnknownEffect",
                payload={"request":effect_request},
                trace_refs=["trace:test-effect-unknown"],
                evidence_refs=[],
                effect_known=False
            )
        self.effects.append({"contract":execution_contract["id"],"request":effect_request})
        return EffectExecutionResult(
            status="Executed",
            payload={"request":effect_request,"effect_index":len(self.effects)},
            trace_refs=["trace:test-effect-executed"],
            evidence_refs=["evidence:test-effect"],
            effect_known=True
        )
