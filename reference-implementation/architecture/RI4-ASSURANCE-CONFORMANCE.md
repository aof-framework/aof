# AOF v1.0 Reference Implementation
## RI-4 — Evidence + Verification + Conformance Runner

**Frozen specification SHA-256:** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-4 adds executable Assurance and Conformance layers without redefining frozen semantics.

### Assurance chain
`Claim -> Evidence -> Verification`

The three are deliberately distinct:
- Claim is an assertion.
- Evidence is observable support with provenance and subject/version binding.
- Verification evaluates Evidence against explicit criteria.

`EvidencePresent != EvidenceSufficient`

`Inconclusive != Verified`

Verification is bound to both subject identity and subject version. A material version change
requires fresh Verification.

### Conformance chain
`Requirement -> TestResult -> RequirementResult -> ConformanceResult`

Canonical aggregation preserves:
- `Blocked != Pass`
- `Inconclusive != Pass`
- applicable mandatory violation -> `NonConformant`
- missing mandatory assessment -> `Inconclusive`
- explicit exceptions/limitations -> `Conditional`
- `Conformance != Maturity`

RI-4 consumes observable Evidence and test outcomes. It does not require private chain-of-thought.
Execution success by itself does not establish Verified Outcome or Conformance.
