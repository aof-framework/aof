from runtime.execution.effect_boundary import EffectBoundary

class ExecutionRuntime:
    def __init__(self, adapter, state_store, trace_recorder, contract_registry, kernel=None):
        self.boundary = EffectBoundary(
            adapter=adapter,
            state_store=state_store,
            trace_recorder=trace_recorder,
            contract_registry=contract_registry,
            kernel=kernel
        )

    def execute(self, contract_id, effect_request, effect_facts):
        return self.boundary.execute(contract_id, effect_request, effect_facts)
