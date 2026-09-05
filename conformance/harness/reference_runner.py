#!/usr/bin/env python3
"""
AOF Conformance Harness Skeleton — Phase 1
Protocol-neutral. No transport/API dependency is assumed.
"""
from dataclasses import dataclass
from typing import Any, Dict, List, Protocol

NORMALIZED_RESULTS = {"Pass", "Fail", "Blocked", "NotApplicable", "Inconclusive"}

class Adapter(Protocol):
    def load_fixture(self, fixture: Dict[str, Any]) -> None: ...
    def execute_step(self, step: Dict[str, Any]) -> Dict[str, Any]: ...
    def collect_evidence(self) -> List[Dict[str, Any]]: ...
    def cleanup(self) -> None: ...

@dataclass
class TestOutcome:
    test_id: str
    result: str
    evidence: List[Dict[str, Any]]
    notes: List[str]

def run_test_case(case: Dict[str, Any], adapter: Adapter) -> TestOutcome:
    """Reference skeleton only. Phase 2+ supplies normative executable evaluators."""
    test_id = case["test_id"]
    evidence = []
    notes = []
    try:
        for fixture in case.get("fixtures", []):
            adapter.load_fixture(fixture)
        observations = [adapter.execute_step(step) for step in case.get("steps", [])]
        evidence = adapter.collect_evidence()
        notes.append(f"Collected {len(observations)} observations.")
        # No implicit Pass: evaluator is intentionally absent in Phase 1.
        result = "Inconclusive"
    except Exception as exc:
        result = "Blocked"
        notes.append(str(exc))
    finally:
        try:
            adapter.cleanup()
        except Exception as exc:
            notes.append(f"Cleanup issue: {exc}")
    assert result in NORMALIZED_RESULTS
    return TestOutcome(test_id, result, evidence, notes)
