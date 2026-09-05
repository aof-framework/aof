# AOF v1.0 Reference Implementation
## RI-1 — Runtime Architecture & Adapter Contract

**Status:** REFERENCE IMPLEMENTATION PHASE 1

RI-1 operationalizes the frozen AOF v1.0 semantics without redefining them.

### Preserved boundaries

- Reasoning != Decision != Authority != Action
- Capability != Authority
- Proposal != AuthorizedDecision
- AgentOutput = UntrustedProposal
- Pending != Pass
- ValidAtCheck != ValidAtEffect
- Claim != Evidence != Verification
- Conformance != Maturity

### Runtime planes

1. Control Plane — Orchestrator, Safety Kernel interface, governance coordination.
2. Reasoning Plane — Agent invocation and untrusted Proposal production.
3. Effect Plane — ExecutionContract consumption and Effect Boundary integration.
4. Assurance Plane — Trace, Evidence, Verification and conformance export.

### Adapter contract

Adapters expose implementation-specific systems through canonical observable AOF semantics.
They MUST NOT mint Authority, suppress Policy Deny, convert Pending to Allow, fabricate Approval,
hide material State change, bypass required Verification, or expand execution scope.

Supported modes: AOFNative, AdapterBasedBrownfield, Hybrid, InFlightIncremental.

RI-1 is transport-neutral and protocol-neutral. It introduces no OpenAPI/REST dependency.

RI-1 intentionally does not execute consequential effects. That requires later Safety Kernel and Effect Boundary integration.
