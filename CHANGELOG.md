# Changelog

This changelog summarizes documented AOF releases and subsequent repository changes. Release entries are based on the linked release records; internal implementation phases are not separate framework releases.

## Unreleased

### Documentation

- Expanded the root README with an AOF overview, governed execution flow, reading guide, repository layout, adoption coverage, and recorded validation results.
- Clarified the relationship between the normative specification, final LTS declaration, and historical component status labels.
- Clarified that the release manifest and root checksums describe the original package, whose ZIP artifacts are absent from this expanded checkout.
- Added this changelog using the existing release notes and audit records.

## v1.0 LTS — 2026-09-05

First frozen long-term-support release baseline of the AI Orchestration Framework.

### Included

- Frozen framework specification for governed, risk-aware orchestration, with humans and organizations as the governance root and agents as bounded operational actors.
- 22 canonical JSON Schema contracts covering core, governance, execution, assurance and outcome, and conformance objects.
- Executable Conformance Suite with requirement mapping, semantic checks, governance and execution tests, assurance, conformance aggregation, and incremental adoption coverage.
- Reference implementation covering the Safety Kernel, execution contracts, effect boundary, state, trace, evidence, verification, and conformance reporting.
- Six-gate LTS release audit, declaration, release manifest, and packaged-release checksums.

### Corrections incorporated before release

- Realigned the `Evidence`, `Verification`, `EscalationPackage`, and `Outcome` schemas with the frozen Appendix E contracts and regenerated the affected Phase 4 fixtures.
- Corrected `Goal.provenance` requiredness to match Appendix E.9.
- Rebuilt conformance traceability against the frozen requirement and invariant registries and 51 reference test definitions, correcting historical mapping defects without changing executable test behavior.

Details: [schema release notes](schemas/RELEASE-NOTES.md) and [conformance traceability notes](conformance/README.md#lts-a3-traceability-hardening).

### Validation recorded at release

- Canonical schema fidelity: 22 / 22; schema reference failures and fixture mismatches: 0.
- Executable Conformance Suite: 170 tests passing reproducibly.
- Reference implementation: 95 tests passing reproducibly.
- Audit gates A1–A6 completed; A5 passed with a release claim constraint.
- Known release blockers: 0 at declaration time.

### Compatibility and scope

- Preserved frozen v1.0 semantics and transport-, protocol-, implementation-, and workflow-agnostic adoption.
- Established JSON Schema as the canonical structural contract; OpenAPI is excluded from the canonical release path.
- Limited reference implementation direct E2E claims to `AOFNative` and `AdapterBasedBrownfield`. The Conformance Suite also supports `Hybrid` and `InFlightIncremental` adoption modes.
- Identified compact runtime objects as reference projections requiring explicit mapping for canonical interchange.
- Preserved the distinction between schema validity, semantic validity, and AOF conformance; conformance claims remain scoped and evidence-backed.

Sources: [release notes](release/RELEASE-NOTES.md), [LTS declaration](release/AOF-v1.0-LTS-Declaration.md), and [final LTS audit report](audit/AOF-v1.0-LTS-Release-Audit-Report.md).
