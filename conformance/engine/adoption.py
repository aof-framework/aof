from dataclasses import dataclass, asdict
from typing import Any, Dict, List

PASS="Pass"; FAIL="Fail"; BLOCKED="Blocked"

@dataclass
class Result:
    test_id: str
    result: str
    observed: Dict[str, Any]
    expected: Dict[str, Any]
    evidence: List[Dict[str, Any]]
    notes: List[str]
    def to_dict(self): return asdict(self)

def evaluate(case: Dict[str, Any]) -> Result:
    tid=case["test_id"]; f=dict(case.get("facts",{})); exp=dict(case.get("expected",{})); o={}
    ev=[{"type":"AdoptionObservation","test_id":tid,"facts":f}]

    if tid=="ECT-ADP-001":  # greenfield
        o["adoption_valid"] = bool(f.get("canonical_controls_present") and f.get("scope_explicit"))
        o["replacement_required"] = False

    elif tid=="ECT-ADP-002":  # brownfield adapter
        o["adoption_valid"] = bool(
            f.get("existing_workflow_preserved")
            and f.get("adapter_exposes_aof_semantics")
            and f.get("mandatory_controls_enforced")
        )
        o["replacement_required"] = not f.get("existing_workflow_preserved",False)

    elif tid=="ECT-ADP-003":  # hybrid
        o["adoption_valid"] = bool(
            f.get("native_components")
            and f.get("adapter_components")
            and f.get("common_governance_boundary")
        )

    elif tid=="ECT-ADP-004":  # in-flight incremental
        o["adoption_valid"] = bool(
            f.get("existing_pipeline_continues")
            and f.get("selected_boundary_governed")
            and f.get("migration_stage_explicit")
        )

    elif tid=="ECT-ADP-005":  # scope explicit
        o["scope_valid"] = bool(
            f.get("included_components")
            and f.get("excluded_components") is not None
            and f.get("profile")
        )

    elif tid=="ECT-ADP-006":  # scoped conformance anti-loophole
        o["scope_abuse"] = bool(f.get("excluded_mandatory_applicable_control"))
        o["claim_valid"] = not o["scope_abuse"]

    elif tid=="ECT-ADP-007":  # adapter semantic equivalence
        o["equivalent"] = bool(
            f.get("identity_preserved")
            and f.get("authority_semantics_preserved")
            and f.get("policy_semantics_preserved")
            and f.get("state_semantics_preserved")
            and f.get("trace_semantics_preserved")
        )

    elif tid=="ECT-ADP-008":  # adapter cannot grant authority
        o["authority_expanded_by_adapter"] = bool(f.get("adapter_inserted") and f.get("authority_expanded"))
        o["valid"] = not o["authority_expanded_by_adapter"]

    elif tid=="ECT-ADP-009":  # adapter cannot suppress deny
        o["deny_suppressed"] = bool(f.get("policy_deny") and not f.get("deny_propagated"))
        o["valid"] = not o["deny_suppressed"]

    elif tid=="ECT-ADP-010":  # transport agnostic
        o["transport_dependency_violation"] = bool(f.get("requires_http_or_rest"))
        o["valid"] = not o["transport_dependency_violation"]

    elif tid=="ECT-ADP-011":  # existing non-AOF tools may remain
        o["replacement_required"] = bool(f.get("requires_replacing_unrelated_tooling"))
        o["valid"] = not o["replacement_required"]

    elif tid=="ECT-ADP-012":  # scope claim cannot exceed evidence
        o["claim_overreach"] = bool(f.get("claim_scope") > f.get("evidence_scope"))
        o["valid"] = not o["claim_overreach"]

    elif tid=="ECT-ADP-013":  # phased control rollout
        o["stage_valid"] = bool(
            f.get("stage_controls_explicit")
            and f.get("known_gaps_declared")
            and f.get("claim_limited_to_current_stage")
        )

    elif tid=="ECT-ADP-014":  # partial adoption != partial compliance
        o["weak_compliance_claim"] = bool(
            f.get("partial_adoption")
            and f.get("claims_full_compliance")
            and not f.get("all_applicable_mandatory_controls_satisfied")
        )
        o["valid"] = not o["weak_compliance_claim"]

    elif tid=="ECT-ADP-015":  # observability through adapter
        o["observable"] = bool(
            f.get("decision_observable")
            and f.get("state_observable")
            and f.get("effect_observable")
            and f.get("evidence_collectable")
        )

    elif tid=="ECT-ADP-016":  # no hidden consequential fields
        o["hidden_consequential_semantics"] = bool(f.get("hidden_fields_change_governance_outcome"))
        o["valid"] = not o["hidden_consequential_semantics"]

    elif tid=="ECT-ADP-017":  # same semantics across adoption modes
        o["semantic_equivalence"] = (
            f.get("native_decision")==f.get("adapter_decision")==f.get("hybrid_decision")
        )

    elif tid=="ECT-ADP-018":  # brownfield revocation
        o["revocation_enforced"] = bool(
            f.get("authority_revoked")
            and f.get("adapter_receives_revocation")
            and not f.get("effect_occurs")
        )

    elif tid=="ECT-ADP-019":  # brownfield trace completeness
        o["trace_complete"] = bool(
            f.get("legacy_event_correlated")
            and f.get("aof_decision_trace")
            and f.get("effect_trace")
        )

    elif tid=="ECT-ADP-020":  # conformance manifest scope
        o["manifest_valid"] = bool(
            f.get("subject")
            and f.get("subject_version")
            and f.get("profile")
            and f.get("scope")
            and f.get("assessment_mode")
        )

    else:
        return Result(tid,BLOCKED,o,exp,ev,["Unknown Phase 6 evaluator"])

    ok=all(o.get(k)==v for k,v in exp.items())
    return Result(tid,PASS if ok else FAIL,o,exp,ev,[])
