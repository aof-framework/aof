from runtime.safety_kernel.kernel import SafetyKernel

class EffectBoundary:
    """Controlled consequential effect boundary.

    Revalidates governance immediately before effect.
    ValidAtCheck != ValidAtEffect is enforced by re-reading state and re-evaluating the Safety Kernel.
    """

    def __init__(self, adapter, state_store, trace_recorder, contract_registry, kernel=None):
        self.adapter = adapter
        self.state_store = state_store
        self.trace = trace_recorder
        self.contracts = contract_registry
        self.kernel = kernel or SafetyKernel()

    def execute(self, contract_id, effect_request, effect_facts):
        contract = self.contracts.get(contract_id)
        if contract is None:
            return self._blocked(contract_id, "EXECUTION_CONTRACT_NOT_FOUND")

        ok, reason = self.contracts.validate_replay(contract_id)
        if not ok:
            return self._blocked(contract_id, reason)

        subject_ref = contract["subject_ref"]
        current = self.state_store.get(subject_ref)
        if current is None:
            return self._blocked(contract_id, "STATE_NOT_FOUND")

        expected_version = str(contract["subject_state_version"])
        if current["version"] != expected_version:
            return self._blocked(contract_id, "STATE_STALE_AT_EFFECT")

        if contract.get("decision_status") != "Allow":
            return self._blocked(contract_id, "DECISION_NOT_ALLOW")

        if not contract.get("authorized", False):
            return self._blocked(contract_id, "EXECUTION_CONTRACT_NOT_AUTHORIZED")

        # Effect-boundary revalidation.
        facts = dict(effect_facts)
        facts["state_valid"] = True
        facts["state_stale"] = False
        decision = self.kernel.evaluate(facts)

        self.trace.append({
            "event_type": "EffectBoundaryRevalidation",
            "execution_ref": contract_id,
            "subject_ref": subject_ref,
            "decision_status": decision.status,
            "execute_allowed": decision.execute_allowed,
            "state_version": current["version"]
        })

        if not decision.execute_allowed:
            status = "Pending" if decision.status == "Pending" else "Blocked"
            return {
                "status": status,
                "effect_occurred": False,
                "reason": "EFFECT_BOUNDARY_REVALIDATION_NOT_ALLOW",
                "decision_status": decision.status
            }

        self.contracts.mark_consumed(contract_id)

        self.trace.append({
            "event_type": "EffectDispatchStarted",
            "execution_ref": contract_id,
            "subject_ref": subject_ref,
            "state_version": current["version"]
        })

        try:
            result = self.adapter.execute_effect(contract, effect_request)
        except Exception as exc:
            self.trace.append({
                "event_type": "EffectDispatchFailed",
                "execution_ref": contract_id,
                "subject_ref": subject_ref,
                "error": type(exc).__name__,
            })
            return {
                "status": "Failed",
                "effect_occurred": False,
                "reason": "ADAPTER_EFFECT_FAILURE",
                "error": type(exc).__name__
            }

        effect_known = getattr(result, "effect_known", True)
        status = getattr(result, "status", "UnknownEffect")

        self.trace.append({
            "event_type": "EffectDispatchCompleted",
            "execution_ref": contract_id,
            "subject_ref": subject_ref,
            "effect_status": status,
            "effect_known": effect_known,
            "trace_refs": getattr(result, "trace_refs", [])
        })

        if not effect_known:
            return {
                "status": "UnknownEffect",
                "effect_occurred": None,
                "reason": "EFFECT_OUTCOME_UNKNOWN",
                "adapter_result": getattr(result, "payload", {})
            }

        return {
            "status": status,
            "effect_occurred": status == "Executed",
            "reason": "EFFECT_DISPATCH_COMPLETE",
            "adapter_result": getattr(result, "payload", {}),
            "trace_refs": getattr(result, "trace_refs", []),
            "evidence_refs": getattr(result, "evidence_refs", [])
        }

    def _blocked(self, contract_id, reason):
        self.trace.append({
            "event_type": "EffectBlocked",
            "execution_ref": contract_id,
            "reason": reason
        })
        return {"status":"Blocked","effect_occurred":False,"reason":reason}
