from runtime.safety_kernel.kernel import SafetyKernel
from runtime.execution.contracts import ExecutionContractRegistry
from runtime.execution.runtime import ExecutionRuntime
from runtime.assurance.verification import VerificationEngine
from runtime.conformance.runner import ConformanceRunner

class ReferenceOrchestrator:
    """Reference end-to-end governed orchestration path."""

    def __init__(self, adapter, state_store, trace_recorder):
        self.adapter=adapter
        self.state=state_store
        self.trace=trace_recorder
        self.kernel=SafetyKernel()
        self.contracts=ExecutionContractRegistry()
        self.execution=ExecutionRuntime(adapter,state_store,trace_recorder,self.contracts,self.kernel)
        self.verification=VerificationEngine()
        self.conformance=ConformanceRunner()

    def prepare(self, request, governance_facts):
        ctx=self.adapter.load_context(request["context_descriptor_ref"])
        proposal_obs=self.adapter.invoke_reasoning(
            request["agent_ref"],request["task_ref"],ctx.payload
        )
        proposal=proposal_obs.payload["proposal"]
        state=self.state.get(request["subject_ref"])
        decision=self.kernel.evaluate(governance_facts)
        self.trace.append({
            "event_type":"GovernanceDecision",
            "request_id":request["request_id"],
            "subject_ref":request["subject_ref"],
            "decision_status":decision.status
        })
        return {"proposal":proposal,"state":state,"decision":decision}

    def issue_execution_contract(self, request, prepared, contract_id):
        decision=prepared["decision"]
        if not decision.execute_allowed:
            return None
        contract={
            "id":contract_id,
            "subject_ref":request["subject_ref"],
            "subject_state_version":prepared["state"]["version"],
            "decision_status":decision.status,
            "authorized":True,
            "single_use":True
        }
        self.contracts.register(contract)
        self.trace.append({
            "event_type":"ExecutionContractIssued",
            "request_id":request["request_id"],
            "execution_ref":contract_id,
            "subject_ref":request["subject_ref"]
        })
        return contract

    def execute(self, contract_id, effect_request, effect_facts):
        return self.execution.execute(contract_id,effect_request,effect_facts)

    def verify_effect(self, subject_ref, subject_version, evidence_items,
                      criteria_ref="criteria:effect", verifier_ref="verifier:reference"):
        return self.verification.verify(
            subject_ref=subject_ref,
            subject_version=subject_version,
            criteria_ref=criteria_ref,
            evidence_items=evidence_items,
            verifier_ref=verifier_ref,
            subject_actor_ref=None,
            independence_required=False
        )

    def report_conformance(self, manifest):
        return self.conformance.run(manifest)
