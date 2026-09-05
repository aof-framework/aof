# AOF v1.0 Executable Conformance Test Suite
## Phase 2 — Core Semantic Tests

**Status:** EXECUTABLE CORE SEMANTICS IMPLEMENTED  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Phase 2 converts foundational frozen AOF semantic separations into executable tests.

## Implemented semantic assertions

1. `Capability != Authority` / `NoGrant => Deny`
2. `Proposal != AuthorizedDecision`
3. `AgentOutput = UntrustedProposal`
4. `HumanUnavailable != Approved`
5. `Pending != Pass`
6. `PolicyPrompt != PolicyEnforcement`
7. `TechnicalAccess != Authority`
8. `Approval != AuthorityGrant`
9. `MandatoryControlFailure => !ImplicitPermit`
10. `ConsequentialEffect => ApplicableSafetyKernelEvaluation`
11. Unknown mandatory policy MUST NOT become implicit Allow
12. `AIAgent != GovernanceRoot`

## Test design

Each executable test has:
- one positive fixture expected to Pass;
- one adversarial/negative mutation expected to be detected as Fail;
- frozen invariant references;
- reference `CT-*` links where the specification provides them;
- conservative Requirement mapping.

The evaluator is protocol-neutral. It does not assume HTTP, OpenAPI, MCP,
a particular Agent runtime, or a particular S-SDLC platform.

## Critical non-invention rule

Some frozen invariants explicitly state:

`No direct mapping asserted; consult Appendix F verification disposition`.

Phase 2 preserves that statement. Those invariants receive executable coverage,
but the package does **not** fabricate a direct Requirement mapping.

## Deferred to later phases

- delegation conservation depth and authority attenuation;
- revocation/TOCTOU at Effect Boundary;
- state concurrency and stale Decision behavior;
- retry/replan/recovery semantics;
- Evidence admissibility and Verification independence;
- Conformance aggregation;
- brownfield scope/adoption scenario suite.
