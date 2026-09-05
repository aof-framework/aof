# AOF v1.0 Reference Implementation — RI-5

**Release:** v1.0 LTS\
**Status:** RELEASED\
**Tanggal rilis:** 2026-09-05\

Bagian dari [rilis AOF v1.0 LTS](../release/AOF-v1.0-LTS-Declaration.md). Hash baseline dan hasil pengujian terdahulu di bawah merupakan provenance rilis asli. Identitas berkas spesifikasi saat ini tersedia dalam [manifest rilis](../release/AOF-v1.0-LTS-Release-Manifest.json) dan [catatan revisi editorial](../release/EDITORIAL-REVISION.md).

**Phase:** RI-5 — End-to-End & Brownfield Validation\
**SHA-256 baseline spesifikasi asli (provenance):** `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`

RI-1 through RI-4 are retained.

RI-5 validates the complete governed reference path:

`Request -> Untrusted Proposal -> Safety Kernel -> ExecutionContract -> Effect Boundary -> Trace -> Evidence -> Verification -> ConformanceReport`

Both `AOFNative` and `AdapterBasedBrownfield` implementations are tested against equivalent observable governance semantics.

Key properties:
- Brownfield adoption does not require destructive workflow replacement.
- Adapter output remains an `UntrustedProposal`.
- revocation and Policy Deny block native and Brownfield effects equivalently.
- State changes after Decision block effect at the Effect Boundary.
- single-use ExecutionContract replay is rejected.
- Trace correlates governance and effect lifecycle.
- Evidence can support Verification but is not Verification itself.
- Conformance claims remain explicitly scoped.

RI-5 telah menyelesaikan LTS Release Audit dan menjadi bagian dari rilis AOF v1.0 LTS.


## LTS-A5 audit status

Hasil final: **PASS_WITH_RELEASE_CLAIM_CONSTRAINT**, sesuai [deklarasi LTS](../release/AOF-v1.0-LTS-Declaration.md). Direct E2E Reference Implementation coverage is claimed for `AOFNative`
and `AdapterBasedBrownfield`. `Hybrid` and `InFlightIncremental` remain supported adoption modes
in the Conformance Suite but are not claimed as dedicated RI-5 E2E adapter implementations.
Runtime compact contracts are reference projections; canonical interchange uses explicit mapping.
