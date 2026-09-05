# AOF v1.0 Executable Conformance Test Suite
## Phase 1 — Test Architecture & Requirement Mapping

**Status:** PHASE 1 BASELINE COMPLETE  
**Normative source:** `Framework Specification v1.0 RC-Final-Public-Readiness-Hardened.md`  
**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

## 1. Purpose

Phase 1 establishes the executable-conformance architecture without inventing new AOF semantics.

Canonical chain:

`Requirement -> Test -> Evidence -> ConformanceResult`

The suite is protocol-neutral and supports:
- AOF-native implementations;
- adapter-based brownfield implementations;
- in-flight incremental adoption.

It does not require REST, OpenAPI, a specific Agent runtime, or a specific S-SDLC toolchain.

## 2. Test taxonomy

1. **Structural** — machine-readable schema checks.
2. **Semantic** — invariant/governance meaning.
3. **Behavioral** — observable runtime and Effect Boundary behavior.
4. **Inspection** — configuration/artifact inspection where runtime stimulation is impractical.

Negative tests are preferred for deny, fail-controlled, non-bypassability, revocation,
stale-state, and isolation properties.

## 3. Result semantics

TestResult:
`Pass | Fail | Blocked | NotApplicable | Inconclusive`

RequirementResult:
`Satisfied | Violated | NotApplicable | Inconclusive`

ConformanceResult:
`Conformant | NonConformant | Conditional | Inconclusive`

Hard boundaries:
- `Blocked != Pass`
- `Inconclusive != Pass`
- `MandatoryViolation => NonConformant`
- `Conformance != Maturity`
- `SchemaValidity != SemanticValidity != AOFConformance`

## 4. Requirement registry

Phase 1 extracted **332** unique explicit AOF Requirement IDs from the frozen specification.
The latest explicit canonical definition is retained where an ID occurs more than once.

This registry is a traceability artifact. Normative meaning remains the frozen specification.

## 5. Reference test catalog

The frozen specification contains **51** direct `CT-*` definitions.

Phase 1 does not force a test onto a Requirement merely because the domain name looks similar.
Only explicit/candidate traceability already present in the frozen specification is recorded as mapped.

Requirements without such mapping remain `PendingExecutableMapping`.

## 6. Brownfield and incremental adoption

AOF conformance is explicitly scoped.

`ScopedAdoption != WeakConformance`

A brownfield implementation MAY use adapters around an existing workflow.
The harness evaluates applicable AOF requirements inside the declared scope without requiring
destructive replacement of the surrounding S-SDLC.

However:

`NotApplicable` MUST NOT be used to hide a mandatory control that the profile/scope actually requires.

## 7. Harness architecture

The reference harness uses a protocol-neutral Adapter interface:

Existing System / AOF-native Runtime
        |
        v
Conformance Adapter
        |
        v
Test Stimulus -> Observable Decision/State/Effect -> Evidence Collector
        |
        v
Requirement Aggregator -> ConformanceReport

The harness MUST NOT create implicit Authority simply to make a test pass.

## 8. Phase boundaries

Phase 1 produces architecture and mapping only.
It intentionally returns `Inconclusive` in the reference runner until Phase 2+ provides executable evaluators.

Next:
- Phase 2: Core Semantic Tests
- Phase 3: Governance & Execution Tests
- Phase 4: Assurance Tests
- Phase 5: Conformance Engine Tests
- Phase 6: Brownfield / Incremental Adoption Tests
