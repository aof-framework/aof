# AOF v1.0 Canonical Machine-Readable Schemas

**Package Status:** FINAL CONSOLIDATED SCHEMA PACKAGE  
**Schema Format:** JSON Schema Draft 2020-12  
**Canonical Contracts:** 22 / 22  
**Frozen Specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

This package is the machine-readable schema realization of the frozen AOF v1.0 semantic model.
It does **not** replace the normative framework specification.

## Semantic boundary

`SchemaValidity != SemanticValidity != AOFConformance`

A structurally valid JSON instance can still violate AOF semantics such as Authority conservation,
Policy mediation, Risk controls, Verification independence, State-transition correctness,
TOCTOU freshness, Safety Kernel non-bypassability, or conformance aggregation rules.

## Contract groups

### Core
Goal, Task, Agent, ContextDescriptor, Resource, Capability

### Governance
AuthorityGrant, Policy, RiskAssessment, Approval

### Execution
ActionProposal, Decision, ExecutionContract, StateTransition, TraceEvent, AgentInteractionContract

### Assurance & Outcome
Evidence, Verification, EscalationPackage, Outcome

### Conformance
ConformanceManifest, ConformanceReport

## Frozen semantic boundaries preserved

- `Reasoning != Decision != Authority != Action`
- `Capability != Authority`
- `Proposal != AuthorizedDecision`
- `Approval != AuthorityGrant`
- `RiskAssessment != RiskAcceptance`
- `Claim != Evidence != Verification`
- `Confidence != Verification`
- `Inconclusive != Verified`
- `Trace != AuthoritativeState`
- `ExecutionContract != AuthorityGrant`
- `Conformance != Maturity`
- `Conformant != ZeroResidualRisk`

## Shared schema consolidation

Phase-local helper files were deduplicated into `common/`.
The 22 canonical contract files are copied byte-for-byte from their validated phase artifacts.
The final helper set is a conservative superset required to resolve all cross-file references.

## OpenAPI

OpenAPI is intentionally not included in this package. A future API binding MAY reference these
canonical JSON Schemas. The JSON Schema contracts remain protocol-neutral.

## Provenance

Normative semantic source:

`Framework Specification v1.0 RC-Final-Public-Readiness-Hardened.md`

SHA-256:

`57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

All release validation details are in `validation/final-validation-report.json`.


## LTS-A2 status

This package is the LTS-A2 hardened schema candidate. All 22 canonical contracts have direct
top-level field fidelity with Appendix E.9-E.30. `SchemaValidity != SemanticValidity != AOFConformance`
remains unchanged.
