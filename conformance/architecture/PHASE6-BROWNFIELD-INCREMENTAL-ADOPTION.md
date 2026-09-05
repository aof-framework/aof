# AOF v1.0 Executable Conformance Test Suite
## Phase 6 — Brownfield / Incremental Adoption Tests

**Status:** EXECUTABLE ADOPTION COMPATIBILITY TESTS IMPLEMENTED  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Phase 6 validates the implementation/adoption model without requiring destructive workflow replacement.

Supported adoption modes:
- Greenfield
- BrownfieldAdapter
- Hybrid
- InFlightIncremental

Core principles tested:
- existing S-SDLC/workflow MAY remain in place;
- an AOF Adapter MAY expose canonical governance semantics around legacy systems;
- adapters MUST NOT expand Authority;
- adapters MUST NOT suppress Policy Deny;
- revocation MUST remain effective through adapter boundaries;
- conformance Evidence MUST remain observable;
- claim scope MUST NOT exceed evidence scope;
- excluded scope MUST NOT hide applicable mandatory controls;
- adoption MUST remain transport/protocol neutral;
- partial adoption MUST NOT be represented as full compliance unless all applicable mandatory controls are satisfied.

Reference architecture:

Existing System
      |
      v
AOF Adapter
      |
      v
Canonical AOF Semantics
      |
      v
Control / Verification / Trace / Conformance

This phase is implementation guidance validation layered on the frozen semantic baseline.
It does not create new frozen normative requirements.
