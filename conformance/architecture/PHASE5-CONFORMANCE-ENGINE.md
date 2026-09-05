# AOF v1.0 Executable Conformance Test Suite
## Phase 5 — Conformance Engine Tests

**Status:** EXECUTABLE CONFORMANCE AGGREGATION IMPLEMENTED  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Canonical chain:

`Requirement -> TestResult -> RequirementResult -> ConformanceResult`

Implemented semantics:
- `Pass`, `Fail`, `Blocked`, `NotApplicable`, `Inconclusive`;
- `Satisfied`, `Violated`, `NotApplicable`, `Inconclusive`;
- `Conformant`, `NonConformant`, `Conditional`, `Inconclusive`;
- mandatory failure propagation;
- mandatory missing/inconclusive coverage protection;
- evidence binding for requirements that require evidence;
- subject/version/profile/scope claim binding;
- explicit exceptions/limitations -> Conditional;
- NotApplicable anti-loophole rules.

Important:
`Blocked != Pass`
`Inconclusive != Pass`
`Conformance != Maturity`
`PartialAdoption != PartialCompliance`

A scoped claim MAY exclude genuinely non-applicable functionality, but claimed scope MUST NOT
be manipulated to omit controls that are actually required by the selected profile and assessed boundary.
