# AOF v1.0 Reference Implementation — RI-5

**Phase:** RI-5 — End-to-End & Brownfield Validation  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-1 through RI-4 are retained.

RI-5 validates the complete governed reference path:

`Request -> Untrusted Proposal -> Safety Kernel -> ExecutionContract -> Effect Boundary -> Trace -> Evidence -> Verification -> ConformanceReport`

Both `AOFNative` and `AdapterBasedBrownfield` implementations are tested against equivalent observable governance semantics.

Key properties:
- Brownfield adoption does not require destructive workflow replacement.
- Adapter output remains an `UntrustedProposal`.
- revocation and Policy Deny block native and Brownfield effects equivalently.
- State changes after Decision block effect at the Effect Boundary.
- single-use ExecutionContract replay is rejected.
- Trace correlates governance and effect lifecycle.
- Evidence can support Verification but is not Verification itself.
- Conformance claims remain explicitly scoped.

RI-5 is the final Reference Implementation phase before LTS Release Audit.


## LTS-A5 audit status

Result: **BLOCKED**. Direct E2E Reference Implementation coverage is claimed for `AOFNative`
and `AdapterBasedBrownfield`. `Hybrid` and `InFlightIncremental` remain supported adoption modes
in the Conformance Suite but are not claimed as dedicated RI-5 E2E adapter implementations.
Runtime compact contracts are reference projections; canonical interchange uses explicit mapping.
