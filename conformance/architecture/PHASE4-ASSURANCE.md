# AOF v1.0 Executable Conformance Test Suite
## Phase 4 — Assurance Tests

**Status:** EXECUTABLE ASSURANCE TESTS IMPLEMENTED  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Phase 4 operationalizes Evidence, Verification, and completion assurance semantics.

Implemented boundaries:
- `Claim != Evidence != Verification`
- `EvidencePresent != EvidenceSufficient`
- consequential Evidence provenance/admissibility;
- stale Evidence handling;
- material contradiction visibility;
- `Inconclusive != Verified`;
- `SelfCheck != IndependentVerification`;
- circular Verification does not create false independence;
- explicit Verification criteria;
- subject/version binding;
- material change -> re-verification;
- `Verified != Authorized`;
- `Verification != Approval`;
- `ExecutionSuccess != VerifiedOutcome`;
- successful completion requires required Verification/assurance.

Assurance evidence is observable process/result evidence.
The suite MUST NOT require private chain-of-thought.

Direct frozen CT anchors used:
`CT-EVD-001`, `CT-VER-001`, `CT-VER-002`, `CT-LC-003`.

Deferred to Phase 5:
- applicability aggregation;
- RequirementResult aggregation;
- profile-level ConformanceResult;
- mandatory failure propagation;
- evidence package completeness for conformance claims.
