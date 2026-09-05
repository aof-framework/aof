from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

PASS="Pass"
FAIL="Fail"
PENDING="Pending"

@dataclass
class GateResult:
    gate: str
    status: str  # Pass | Fail | Pending
    reason_code: str
    subject_ref: Optional[str] = None
    evidence_refs: List[str] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SafetyKernelDecision:
    status: str  # Allow | Deny | Pending
    execute_allowed: bool
    gate_results: Dict[str, GateResult]
    reason_codes: List[str] = field(default_factory=list)
