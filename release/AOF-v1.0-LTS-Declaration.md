# AI Orchestration Framework (AOF) v1.0 LTS — Declaration

**Release:** AOF v1.0 LTS\
**Release date:** 2026-09-05\
**Status:** RELEASED\
**SHA-256 spesifikasi saat ini (LTS-Editorial-2):** `6197f71416984cca1811d5cd0cdd30327cccb9026acc5b92509f8f2a3a137974`
**SHA-256 baseline asli (provenance):** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

## Declaration

The AI Orchestration Framework (AOF) v1.0 is hereby declared **Long-Term Support (LTS)**.

This declaration follows completion of the Semantic Freeze, canonical machine-readable schema
packaging, Executable Conformance Test Suite, Reference Implementation, and the six-gate LTS
Release Audit.

The LTS release preserves the frozen governance model in which Human/Organization remains the
Governance Root and an Agent remains a Bounded Operational Actor.

## Frozen semantic boundaries

The release preserves, among others, these boundaries:

- `Reasoning != Decision != Authority != Action`
- `Capability != Authority`
- `Proposal != AuthorizedDecision`
- `AgentOutput = UntrustedProposal`
- `PolicyPrompt != PolicyEnforcement`
- `Approval != AuthorityGrant`
- `RiskAssessment != RiskAcceptance`
- `Pending != Pass`
- `Claim != Evidence != Verification`
- `SchemaValidity != SemanticValidity != AOFConformance`
- `Conformance != Maturity`
- `ScopedAdoption != WeakConformance`
- `PartialAdoption != PartialCompliance`

The executable safety predicate remains:

`ExecuteAllowed = C ∧ H ∧ P ∧ S ∧ R ∧ V`

where an unresolved mandatory gate does not become implicit permission.

## Canonical machine-readable contract

JSON Schema is the canonical structural contract for AOF v1.0 LTS.

`SchemaValidity != SemanticValidity != AOFConformance`

OpenAPI is not part of the AOF v1.0 LTS canonical release contract, dependency graph, conformance
profile, or release criteria. AOF remains transport-, protocol-, and implementation-agnostic.

## Adoption

AOF v1.0 LTS supports greenfield and brownfield/incremental adoption. Adoption does not require
destructive replacement of an existing S-SDLC workflow.

`AOFAdoption != BigBangMigration`

Conformance claims remain explicitly scoped and evidence-backed.

## Reference Implementation claim

The Reference Implementation directly validates AOFNative and AdapterBasedBrownfield. Hybrid and InFlightIncremental are supported adoption modes in the Executable Conformance Suite and are not claimed as dedicated Reference Implementation E2E adapter implementations.

Compact runtime objects are reference projections. They are not claimed to be byte-identical
canonical JSON Schema serializations; canonical interchange requires the documented mapping.

## Release audit

All technical LTS audit gates completed successfully:

- LTS-A1 — Specification Integrity: PASS
- LTS-A2 — Canonical Schema Fidelity: PASS
- LTS-A3 — Requirement / Invariant / Test Traceability: PASS
- LTS-A4 — Executable Conformance Suite Audit: PASS
- LTS-A5 — Reference Implementation Audit: PASS WITH RELEASE CLAIM CONSTRAINT
- LTS-A6 — Cross-Artifact Consistency & Release Hygiene: PASS

At declaration time:

- Known semantic blockers: 0
- Known schema drift: 0
- Broken canonical references: 0
- Conformance Suite failures: 0
- Reference Implementation failures: 0
- Unresolved critical traceability defects: 0

## LTS baseline

Manifest dan checksum aktif mendeskripsikan berkas revisi editorial saat ini. Metadata paket asli tetap tersedia dalam [arsip provenance](provenance/original-v1.0-LTS/README.md). [Catatan revisi editorial](EDITORIAL-REVISION.md) menjelaskan pemisahan keduanya; tanggal deklarasi dan semantik v1.0 tetap dipertahankan.

Future maintenance releases in the v1.0 LTS line MUST preserve the frozen v1.0 semantics unless
a separately governed specification revision explicitly changes them.

**AOF v1.0 LTS is released.**
