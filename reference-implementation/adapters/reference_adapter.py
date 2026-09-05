from runtime.interfaces.adapter import AdapterObservation

class ReferenceAdapter:
    def __init__(self, state=None):
        self._state = state or {}

    def load_context(self, context_descriptor_ref):
        return AdapterObservation({"context_descriptor_ref":context_descriptor_ref,"context":{}},["trace:context-loaded"])

    def invoke_reasoning(self, agent_ref, task_ref, context_snapshot):
        return AdapterObservation({"proposal":{"agent_ref":agent_ref,"task_ref":task_ref,"status":"UntrustedProposal"}},["trace:proposal-produced"])

    def resolve_governance_inputs(self, proposal, subject_state):
        return AdapterObservation({
            "proposal":proposal,"subject_state":subject_state,
            "authority_grants":[],"policies":[],"risk_assessment":None,"verification_state":None
        },["trace:governance-inputs-resolved"])

    def observe_state(self, subject_ref):
        state=self._state.get(subject_ref,{})
        return AdapterObservation({"subject_ref":subject_ref,"state":state,"state_version":str(state.get("version","0"))},["trace:state-observed"])

    def execute_effect(self, execution_contract, effect_request):
        raise NotImplementedError("RI-1 does not execute consequential effects.")

    def collect_evidence(self, subject_ref, event_refs):
        return AdapterObservation({"subject_ref":subject_ref,"event_refs":list(event_refs)},["trace:evidence-collection-requested"],[])

    def cleanup_or_reconcile(self, execution_ref):
        return AdapterObservation({"execution_ref":execution_ref,"status":"NoOpReference"},["trace:cleanup-reconcile"])
