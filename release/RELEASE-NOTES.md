# AOF v1.0 LTS — Release Notes

Release date: 2026-09-05

AOF v1.0 LTS is the first frozen long-term-support release baseline of the AI Orchestration
Framework.

## Included release artifacts

- Frozen Framework Specification
- 22-contract canonical JSON Schema package
- Audited Executable Conformance Suite
- Audited Reference Implementation
- Complete LTS Release Audit
- LTS Declaration, release manifest, and cryptographic checksums

## Validation summary

- Canonical schema fidelity: 22 / 22
- Schema `$ref` failures: 0
- Schema fixture mismatches: 0
- Executable Conformance Suite: 170 tests passing reproducibly
- Reference Implementation: 95 tests passing reproducibly
- LTS audit gates A1-A6: completed
- Known release blockers: 0

## Compatibility position

AOF remains transport-, protocol-, implementation-, and workflow-agnostic. OpenAPI is excluded
from the v1.0 LTS canonical release path.

AOF can be adopted at the beginning of an S-SDLC or introduced incrementally into an existing
workflow through scoped governance integration and adapters.

## Reference Implementation scope

The Reference Implementation directly validates AOFNative and AdapterBasedBrownfield. Hybrid and InFlightIncremental are supported adoption modes in the Executable Conformance Suite and are not claimed as dedicated Reference Implementation E2E adapter implementations.
