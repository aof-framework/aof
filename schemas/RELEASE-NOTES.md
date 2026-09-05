# AOF v1.0 Schema Package — Release Notes

Release: **1.0**  
Date: **2026-09-04**  
Status: **Final Consolidated Schema Package**

This release consolidates Phase 1 through Phase 5 into one canonical JSON Schema package.

No AOF semantic requirement is introduced, removed, strengthened, or weakened by this consolidation.
All 22 canonical contract files are byte-identical to their individually validated phase versions.

Frozen specification provenance:
`57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

Validation gates for this package:
- 22/22 canonical contracts present
- unique canonical `$id` values
- JSON Schema Draft 2020-12 meta-schema validation
- global relative `$ref` resolution
- complete phase fixture replay
- canonical contract byte-identity verification
- package checksum manifest


## LTS-A2 Fidelity Hardening

Direct comparison against frozen Appendix E identified machine-readable extraction drift in
`Evidence`, `Verification`, `EscalationPackage`, and `Outcome`. These four contracts were
realigned to Appendix E.21, E.22, E.27, and E.28. No frozen normative semantics were changed.
Phase 4 fixtures were regenerated against the corrected contracts.

LTS-A2 also corrected `Goal.provenance` requiredness to match the complete Appendix E.9 reference shape.
