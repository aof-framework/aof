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

def subset(child,parent): return set(child).issubset(set(parent))

def active_at(grant,t):
    if grant.get("status")!="Active": return False
    if grant.get("valid_from") is not None and t < grant["valid_from"]: return False
    if grant.get("valid_until") is not None and t > grant["valid_until"]: return False
    return True

def evaluate(case):
    tid=case["test_id"]; f=dict(case.get("facts",{})); exp=dict(case.get("expected",{})); o={}
    ev=[{"type":"GovernanceExecutionObservation","test_id":tid,"facts":f}]
    if tid=="ECT-GEX-001":
        o["delegation_valid"]=subset(f["child_operations"],f["parent_operations"]) and subset(f["child_resources"],f["parent_resources"]) and f["child_risk_ceiling"]<=f["parent_risk_ceiling"]
    elif tid=="ECT-GEX-002":
        o["valid_at_decision"]=active_at(f["grant_at_decision"],f["decision_time"])
        o["valid_at_effect"]=active_at(f["grant_at_effect"],f["effect_time"])
        o["effect_allowed"]=bool(o["valid_at_effect"] and f.get("other_gates_pass",False))
    elif tid=="ECT-GEX-003":
        o["effect_allowed"]=bool(active_at(f["grant"],f["effect_time"]) and f.get("other_gates_pass",False))
    elif tid=="ECT-GEX-004":
        eff=f.get("policy_effects",[])
        o["effective_policy"]="Deny" if "Deny" in eff else ("Allow" if "Allow" in eff else "Pending")
        o["effect_allowed"]=o["effective_policy"]=="Allow"
    elif tid=="ECT-GEX-005":
        r=f.get("mandatory_policy_result")
        o["effect_allowed"]=False if r in (None,"Unknown","Pending") else r=="Allow"
    elif tid=="ECT-GEX-006":
        o["within_risk_ceiling"]=f["action_risk"]<=f["authority_risk_ceiling"]
        o["effect_allowed"]=bool(o["within_risk_ceiling"] and f.get("other_gates_pass",False))
    elif tid=="ECT-GEX-007":
        o["effect_allowed"]=bool(f.get("execution_contract_valid") and f.get("other_gates_pass"))
        o["missing_contract_blocked"]=not f.get("execution_contract_valid",False)
    elif tid=="ECT-GEX-008":
        o["replay_detected"]=bool(f.get("single_use") and f.get("already_consumed") and f.get("replay_attempt"))
        o["effect_allowed"]=not o["replay_detected"]
    elif tid=="ECT-GEX-009":
        o["state_fresh"]=f.get("decision_state_version")==f.get("current_state_version")
        o["effect_allowed"]=bool(o["state_fresh"] and f.get("other_gates_pass",False))
    elif tid=="ECT-GEX-010":
        o["transition_allowed"]=bool(f.get("transition_in_state_machine") and f.get("transition_authorized"))
    elif tid=="ECT-GEX-011":
        o["within_retry_bound"]=f["attempt"]<=f["max_attempts"]
        o["retry_allowed"]=bool(o["within_retry_bound"] and f.get("retry_authorized",False))
    elif tid=="ECT-GEX-012":
        o["authority_expanded"]=not subset(f["retry_operations"],f["original_operations"]) or not subset(f["retry_resources"],f["original_resources"])
        o["retry_allowed"]=not o["authority_expanded"]
    elif tid=="ECT-GEX-013":
        changed=bool(f.get("goal_changed") or f.get("resource_scope_changed") or f.get("risk_changed"))
        o["new_decision_required"]=changed
        o["reuse_old_decision_allowed"]=not changed
    elif tid=="ECT-GEX-014":
        o["effect_allowed"]=bool(f.get("authorized_decision") and f.get("effect_boundary_revalidated"))
    elif tid=="ECT-GEX-015":
        o["authority_created_by_contract"]=bool(f.get("execution_contract") and f.get("authority_created"))
        o["separation_preserved"]=bool(f.get("execution_contract") and not f.get("authority_created"))
    elif tid=="ECT-GEX-016":
        o["trace_complete"]=bool(f.get("decision_trace") and f.get("effect_trace"))
        o["conformance_observable"]=o["trace_complete"]
    else:
        return Result(tid,BLOCKED,o,exp,ev,["Unknown evaluator"])
    ok=all(o.get(k)==v for k,v in exp.items())
    return Result(tid,PASS if ok else FAIL,o,exp,ev,[])
