# AOF v1.0 Executable Conformance Test Suite
## Phase 3 — Governance & Execution Tests

**Status:** EXECUTABLE GOVERNANCE/EXECUTION TESTS IMPLEMENTED  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Coverage:
- delegation conservation and attenuation;
- Authority revocation and expiry;
- `ValidAtCheck != ValidAtEffect`;
- Policy precedence and unknown mandatory Policy;
- Risk ceiling enforcement;
- ExecutionContract requirement and separation from Authority;
- single-use/replay protection;
- stale State and unauthorized transition rejection;
- bounded Retry and no Authority expansion on Retry;
- material Replan -> fresh Decision;
- `Decision != Effect`;
- consequential Trace observability.

Transport remains implementation-defined. No OpenAPI dependency exists.
