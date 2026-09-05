# AOF v1.0 Reference Implementation
## RI-5 — End-to-End & Brownfield Validation

Frozen specification SHA-256: `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-5 validates the complete reference path:

`Request -> Context -> Reasoning -> Untrusted Proposal -> Governance Decision -> ExecutionContract -> Effect Boundary Revalidation -> Effect -> Trace -> Evidence -> Verification -> ConformanceReport`

Two implementation modes are exercised against the same observable governance semantics:

- `AOFNative`
- `AdapterBasedBrownfield`

The Brownfield adapter does not replace the existing runtime. It constrains and observes it through the AOF governance boundary.

Key validation rules:

- Agent/legacy reasoning output remains `UntrustedProposal`.
- `Capability != Authority`.
- `Decision Allow` is insufficient without Effect Boundary revalidation.
- revocation, Policy Deny, stale State, or inconclusive Verification can block the effect.
- adapter cannot broaden Authority or suppress Deny.
- single-use ExecutionContract rejects replay.
- Trace correlates governance and effect events.
- Evidence remains distinct from Verification.
- Conformance is explicitly bound to subject, version, profile, and scope.
- Native and Brownfield modes produce equivalent governance outcomes for equivalent semantic inputs.

RI-5 adds no new frozen normative semantics.
