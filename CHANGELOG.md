# Changelog

Changelog ini merangkum rilis AOF yang terdokumentasi dan perubahan repository setelahnya. Setiap entri rilis mengacu pada catatan rilis yang ditautkan; fase implementasi internal tidak diperlakukan sebagai rilis framework tersendiri.

Bahasa Indonesia digunakan sebagai bahasa utama. Istilah teknis kanonis, identifier, nama komponen, state, dan normative keywords dipertahankan dalam English sesuai konvensi spesifikasi AOF.

## Belum dirilis

### Konsistensi metadata — LTS-Editorial-1

- Menyeragamkan status rilis aktif menjadi `v1.0 LTS — RELEASED` dengan tanggal rilis tetap `2026-09-05`.
- Menyelaraskan hasil audit aktif A4 dan A5 dengan deklarasi final serta memberi konteks historis pada Appendix G–W dan artefak audit.
- Memisahkan hash spesifikasi revisi editorial dari provenance baseline asli; memperbarui manifest dan checksum aktif.
- Menyimpan metadata paket asli dalam arsip provenance tanpa mengubah Requirement, Invariant, kontrak schema, atau perilaku runtime.

### Dokumentasi

- Melengkapi README di root dengan gambaran AOF, alur eksekusi dengan tata kelola, panduan membaca, struktur repository, cakupan adopsi, dan hasil validasi yang tercatat.
- Memperjelas hubungan antara spesifikasi normatif, deklarasi LTS final, dan label status historis pada dokumen komponen.
- Menjelaskan bahwa release manifest dan checksum di root mendeskripsikan paket asli, sedangkan artefak ZIP tidak tersedia dalam checkout yang berisi komponen hasil ekstraksi ini.
- Menambahkan changelog berdasarkan catatan rilis dan audit yang tersedia.
- Menyesuaikan README dan CHANGELOG agar menggunakan Bahasa Indonesia sebagai bahasa utama dengan mempertahankan istilah teknis English sesuai konvensi AOF.

## v1.0 LTS — 2026-09-05

Baseline rilis Long-Term Support (LTS) pertama AI Orchestration Framework dengan semantik yang dibekukan.

### Komponen rilis

- Spesifikasi framework yang dibekukan untuk orkestrasi dengan tata kelola dan kontrol risiko, dengan manusia dan organisasi sebagai Governance Root serta Agent sebagai Bounded Operational Actor.
- 22 kontrak JSON Schema kanonis yang mencakup objek Core, Governance, Execution, Assurance & Outcome, dan Conformance.
- Executable Conformance Suite yang mencakup pemetaan Requirement, pemeriksaan semantik, pengujian Governance dan Execution, Assurance, agregasi Conformance, serta adopsi bertahap.
- Reference Implementation yang mencakup Safety Kernel, ExecutionContract, Effect Boundary, State, Trace, Evidence, Verification, dan pelaporan Conformance.
- Audit rilis LTS dengan enam gate, deklarasi, release manifest, dan checksum paket rilis.

### Perbaikan sebelum rilis

- Menyelaraskan schema `Evidence`, `Verification`, `EscalationPackage`, dan `Outcome` dengan kontrak Appendix E yang dibekukan serta membuat ulang fixture Phase 4 yang terdampak.
- Memperbaiki ketentuan wajib untuk `Goal.provenance` agar sesuai dengan Appendix E.9.
- Membangun ulang ketertelusuran Conformance berdasarkan registry Requirement dan Invariant yang dibekukan serta 51 definisi reference test, sekaligus memperbaiki pemetaan historis tanpa mengubah perilaku executable test.

Rincian: [catatan rilis schema](schemas/RELEASE-NOTES.md) dan [catatan ketertelusuran Conformance](conformance/README.md#lts-a3-traceability-hardening).

### Validasi yang tercatat saat rilis

- Kesesuaian schema kanonis: 22 / 22; kegagalan referensi schema dan ketidaksesuaian fixture: 0.
- Executable Conformance Suite: 170 test lulus secara reproducible.
- Reference Implementation: 95 test lulus secara reproducible.
- Gate audit A1–A6 selesai; A5 lulus dengan batasan klaim rilis.
- Release blocker yang diketahui: 0 pada saat deklarasi.

### Kompatibilitas dan cakupan

- Mempertahankan semantik v1.0 yang dibekukan serta adopsi yang independen terhadap transport, protokol, implementasi, dan workflow.
- Menetapkan JSON Schema sebagai kontrak struktural kanonis; OpenAPI tidak termasuk dalam jalur rilis kanonis.
- Membatasi klaim E2E langsung Reference Implementation pada `AOFNative` dan `AdapterBasedBrownfield`. Conformance Suite juga mendukung mode adopsi `Hybrid` dan `InFlightIncremental`.
- Menetapkan objek runtime ringkas sebagai proyeksi referensi yang memerlukan pemetaan eksplisit untuk pertukaran data dalam bentuk kanonis.
- Mempertahankan perbedaan antara SchemaValidity, SemanticValidity, dan AOFConformance; klaim Conformance tetap memiliki scope yang eksplisit dan didukung Evidence.

Sumber: [catatan rilis](release/RELEASE-NOTES.md), [deklarasi LTS](release/AOF-v1.0-LTS-Declaration.md), dan [laporan audit LTS final](audit/AOF-v1.0-LTS-Release-Audit-Report.md).
