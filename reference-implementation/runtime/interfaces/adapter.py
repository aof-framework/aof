from dataclasses import dataclass, field
from typing import Any, Dict, List, Protocol

@dataclass
class AdapterObservation:
    payload: Dict[str, Any]
    trace_refs: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)

@dataclass
class EffectExecutionResult:
    status: str
    payload: Dict[str, Any]
    trace_refs: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)
    effect_known: bool = True

class RuntimeAdapter(Protocol):
    def load_context(self, context_descriptor_ref: str) -> AdapterObservation: ...
    def invoke_reasoning(self, agent_ref: str, task_ref: str, context_snapshot: Dict[str, Any]) -> AdapterObservation: ...
    def resolve_governance_inputs(self, proposal: Dict[str, Any], subject_state: Dict[str, Any]) -> AdapterObservation: ...
    def observe_state(self, subject_ref: str) -> AdapterObservation: ...
    def execute_effect(self, execution_contract: Dict[str, Any], effect_request: Dict[str, Any]) -> EffectExecutionResult: ...
    def collect_evidence(self, subject_ref: str, event_refs: List[str]) -> AdapterObservation: ...
    def cleanup_or_reconcile(self, execution_ref: str) -> AdapterObservation: ...
