# AI Orchestration Framework (AOF)

**Version:** v1.0 LTS · **Release date:** 2026-09-05

AOF defines a governed, risk-aware model for coordinating AI and non-AI actors through explicit goals, tasks, authority, policy, decisions, actions, evidence, and verification. Humans and organizations remain the governance root; agents operate within delegated authority and accountable boundaries.

The primary reference domain is the Secure Software Development Lifecycle (S-SDLC). AOF can also support other orchestration domains and remains model-, tool-, platform-, transport-, and implementation-agnostic.

## How AOF works

An agent's output is an **untrusted proposal**. Technical capability, reasoning, or a proposed plan does not grant permission to act. AOF separates these concepts:

```text
Reasoning != Decision != Authority != Action
Capability != Authority
Claim != Evidence != Verification
```

The reference implementation demonstrates this governed path:

```text
Request -> Untrusted Proposal -> Safety Kernel -> ExecutionContract
        -> Effect Boundary -> Trace -> Evidence -> Verification -> ConformanceReport
```

The Safety Kernel evaluates six gates: **Capability, Authority, Policy, State, Risk, and Verification**. Execution is allowed only when every gate passes. A failed gate denies execution; an unresolved mandatory gate keeps it pending without permission to execute.

AOF supports bounded autonomy with risk-proportional controls. Human governance does not require human approval for every low-risk operation.

## Start here

| Resource | Purpose |
| --- | --- |
| [LTS declaration](release/AOF-v1.0-LTS-Declaration.md) | Final release status, frozen boundaries, and claim constraints |
| [Framework specification](specification/AOF-v1.0-Framework-Specification.md) | Normative semantics, requirements, invariants, and profiles; primarily Bahasa Indonesia with English technical terms |
| [Canonical schemas](schemas/README.md) | 22 structural contracts using JSON Schema Draft 2020-12 |
| [Executable Conformance Suite](conformance/README.md) | Requirement-to-test traceability and evidence-based conformance evaluation |
| [Reference implementation](reference-implementation/README.md) | Python implementation of the governed execution path |
| [LTS audit report](audit/AOF-v1.0-LTS-Release-Audit-Report.md) | Results of release audit gates A1–A6 |
| [Changelog](CHANGELOG.md) | Release history and repository documentation changes |

The frozen specification is the normative semantic authority. The LTS declaration records the final release decision. Earlier candidate, freeze-hold, or blocked labels retained in component documents and historical audit records should be read in that context.

## Repository layout

```text
specification/             Frozen framework specification
schemas/                   Canonical contracts, fixtures, and validation records
conformance/               Evaluation engines, tests, profiles, and traceability
reference-implementation/  Runtime, adapters, tests, and evidence
audit/                     Release audit findings and validation records
release/                   LTS declaration, release notes, and manifest
README.md                  Project overview and reading guide
CHANGELOG.md               Documented change history
SHA256SUMS.txt             Original packaged-release checksums
```

This checkout contains expanded component files. The [release manifest](release/AOF-v1.0-LTS-Release-Manifest.json) and [root checksums](SHA256SUMS.txt) describe the original packaged release, including ZIP artifacts that are absent from this checkout. The root checksum list also records the original release README; it is not a checksum inventory for this edited working tree.

## Adoption and conformance

AOF can be introduced at the start of an S-SDLC or integrated incrementally into an existing workflow through scoped governance controls and adapters.

| Adoption mode | Executable Conformance Suite | Reference implementation direct E2E coverage |
| --- | --- | --- |
| `AOFNative` | Supported | Yes |
| `AdapterBasedBrownfield` | Supported | Yes |
| `Hybrid` | Supported | Not claimed |
| `InFlightIncremental` | Supported | Not claimed |

Conformance claims must identify their scope and profile and provide supporting evidence. Scoped adoption preserves all mandatory requirements applicable to that scope.

The [profile definitions](conformance/profiles/profile-definitions.json) distinguish base profiles (`AOF-Core`, `AOF-Governed`, `AOF-Assured`), the `AOF-Secure-SDLC` domain profile, and the `AOF-High-Assurance` strengthening profile. Profiles are not a universal maturity ladder.

```text
SchemaValidity != SemanticValidity != AOFConformance
Conformance != Maturity
```

JSON Schema is the canonical structural contract. OpenAPI is excluded from the v1.0 LTS canonical release path. Compact runtime objects are reference projections; canonical interchange requires the documented [runtime-to-canonical mapping](reference-implementation/architecture/LTS-A5-RUNTIME-CANONICAL-MAPPING.json).

## Recorded release validation

The [release notes](release/RELEASE-NOTES.md) and final audit report the following results for the released baseline:

| Check | Recorded result |
| --- | --- |
| Canonical schema fidelity | 22 / 22 contracts |
| Schema reference failures / fixture mismatches | 0 / 0 |
| Executable Conformance Suite | 170 tests passing reproducibly |
| Reference implementation | 95 tests passing reproducibly |
| LTS audit gates | A1–A6 completed; A5 passed with a release claim constraint |
| Known release blockers | 0 at declaration time |

These are recorded release results, not a claim that tests have been rerun for every checkout. Future maintenance in the v1.0 LTS lineage must preserve frozen semantics unless an explicitly governed specification revision changes them.
