# AI Orchestration Framework (AOF)

[![CI](https://github.com/aof-framework/aof/actions/workflows/ci.yml/badge.svg)](https://github.com/aof-framework/aof/actions/workflows/ci.yml)
[![CodeQL](https://github.com/aof-framework/aof/actions/workflows/codeql.yml/badge.svg)](https://github.com/aof-framework/aof/actions/workflows/codeql.yml)

**Versi:** v1.0 LTS · **Status:** RELEASED · **Tanggal rilis:** 2026-09-05

AOF mendefinisikan model orkestrasi dengan tata kelola dan kontrol risiko untuk mengoordinasikan aktor AI dan non-AI melalui `Goal`, `Task`, `Authority`, `Policy`, `Decision`, `Action`, `Evidence`, dan `Verification` yang eksplisit. Manusia dan organisasi tetap menjadi Governance Root; Agent beroperasi dalam batas kewenangan yang didelegasikan dan dapat dipertanggungjawabkan.

Domain rujukan utamanya adalah Secure Software Development Lifecycle (S-SDLC). AOF juga dapat diterapkan pada domain orkestrasi lain dan tetap independen terhadap model, tool, platform, transport, protokol, serta implementasi.

Dokumentasi ini menggunakan Bahasa Indonesia sebagai bahasa utama. Istilah teknis kanonis, identifier, nama komponen, state, dan normative keywords dipertahankan dalam English sesuai konvensi spesifikasi AOF.

## Cara kerja AOF

Keluaran Agent merupakan **Untrusted Proposal**. Kemampuan teknis, reasoning, atau rencana yang diusulkan tidak dengan sendirinya memberikan izin untuk bertindak. AOF memisahkan konsep berikut:

```text
Reasoning != Decision != Authority != Action
Capability != Authority
Claim != Evidence != Verification
```

Reference Implementation memperagakan alur eksekusi dengan tata kelola berikut:

```text
Request -> Untrusted Proposal -> Safety Kernel -> ExecutionContract
        -> Effect Boundary -> Trace -> Evidence -> Verification -> ConformanceReport
```

Safety Kernel mengevaluasi enam gate: **Capability, Authority, Policy, State, Risk, dan Verification**. Eksekusi hanya diizinkan ketika seluruh gate berstatus `Pass`. Gate yang berstatus `Fail` menghasilkan `Deny`; gate wajib yang belum terselesaikan menghasilkan `Pending` tanpa izin eksekusi.

AOF mendukung otonomi terbatas dengan kontrol yang sebanding dengan risiko. Human governance tidak mengharuskan persetujuan manusia untuk setiap operasi berisiko rendah.

## Mulai cepat

Repository ini mendistribusikan spesifikasi, schema, Conformance Suite, dan Reference Implementation; bukan paket Python yang diinstal untuk production. Untuk menjalankan validasi lokal:

```bash
git clone https://github.com/aof-framework/aof.git
cd aof
python -m venv .venv
```

Aktifkan virtual environment dengan `. .venv/bin/activate` pada shell POSIX atau `.venv\Scripts\Activate.ps1` pada PowerShell, lalu pasang dependensi:

```bash
python -m pip install -r requirements-dev.txt
```

Jalankan kedua test suite dari direktori masing-masing:

```bash
cd conformance
python -m pytest -q -p no:cacheprovider
cd ../reference-implementation
python -m pytest -q -p no:cacheprovider
```

Contoh evaluasi Safety Kernel tersedia dalam [test kernel](reference-implementation/tests/safety_kernel/test_kernel.py) dan [fixture SK-001](reference-implementation/fixtures/safety_kernel/SK-001.json). Keputusan `Allow` hanya dihasilkan ketika seluruh gate wajib berstatus `Pass`.

## Panduan membaca

| Dokumen | Isi dan kegunaan |
| --- | --- |
| [Deklarasi LTS](release/AOF-v1.0-LTS-Declaration.md) | Status rilis final, batas semantik yang dibekukan, dan batasan klaim |
| [Spesifikasi framework](specification/AOF-v1.0-Framework-Specification.md) | Semantik normatif, Requirement, Invariant, dan Profile |
| [Canonical Schemas](schemas/README.md) | 22 kontrak struktural menggunakan JSON Schema Draft 2020-12 |
| [Executable Conformance Suite](conformance/README.md) | Ketertelusuran Requirement ke Test dan evaluasi Conformance berbasis Evidence |
| [Reference Implementation](reference-implementation/README.md) | Implementasi Python untuk alur eksekusi dengan tata kelola |
| [Laporan audit LTS](audit/AOF-v1.0-LTS-Release-Audit-Report.md) | Hasil audit rilis pada gate A1–A6 |
| [Changelog](CHANGELOG.md) | Riwayat rilis dan perubahan dokumentasi repository |

Spesifikasi yang dibekukan menjadi sumber otoritatif untuk semantik normatif. Deklarasi LTS mencatat keputusan rilis final. Label candidate, freeze-hold, atau blocked dari tahap sebelumnya yang masih tersimpan dalam dokumen komponen dan catatan audit historis perlu dibaca dalam konteks tersebut.

## Struktur repository

```text
specification/             Spesifikasi framework yang dibekukan
schemas/                   Kontrak kanonis, fixture, dan catatan validasi
conformance/               Engine evaluasi, test, profile, dan ketertelusuran
reference-implementation/  Runtime, adapter, test, dan evidence
audit/                     Temuan audit rilis dan catatan validasi
release/                   Deklarasi LTS, catatan rilis, dan manifest
.github/                   CI, security scanning, template, dan CODEOWNERS
tools/                     Validator release, checksum, dan formula
README.md                  Gambaran proyek dan panduan membaca
CHANGELOG.md               Riwayat perubahan yang terdokumentasi
CONTRIBUTING.md            Panduan kontribusi dan change control
SECURITY.md                Prosedur pelaporan kerentanan
LICENSE                    Apache License 2.0
SHA256SUMS.txt             Checksum berkas repository saat ini
```

Checkout ini berisi komponen hasil ekstraksi dengan metadata `LTS-Editorial-2`. Revisi ini membuat 985 formula kompatibel dengan math rendering GitHub tanpa mengubah makna normatifnya. [Manifest aktif](release/AOF-v1.0-LTS-Release-Manifest.json) dan [checksum aktif](SHA256SUMS.txt) menunjuk berkas saat ini. Metadata serta checksum paket asli disimpan terpisah dalam [arsip provenance](release/provenance/original-v1.0-LTS/README.md); ZIP historis tidak tersedia dalam checkout ini. [Catatan revisi editorial](release/EDITORIAL-REVISION.md) menjelaskan perubahan dan provenance-nya.

## Adopsi dan Conformance

AOF dapat diterapkan sejak awal S-SDLC atau diintegrasikan secara bertahap ke workflow yang sudah berjalan melalui kontrol tata kelola dengan scope yang eksplisit dan adapter.

| Mode adopsi | Executable Conformance Suite | Cakupan E2E langsung pada Reference Implementation |
| --- | --- | --- |
| `AOFNative` | Didukung | Ya |
| `AdapterBasedBrownfield` | Didukung | Ya |
| `Hybrid` | Didukung | Tidak diklaim |
| `InFlightIncremental` | Didukung | Tidak diklaim |

Klaim Conformance harus menyatakan scope dan Profile serta menyertakan Evidence pendukung. Adopsi dengan scope terbatas tetap mempertahankan seluruh Requirement wajib yang berlaku dalam scope tersebut.

[Definisi Profile](conformance/profiles/profile-definitions.json) membedakan BaseProfile (`AOF-Core`, `AOF-Governed`, `AOF-Assured`), DomainProfile `AOF-Secure-SDLC`, dan StrengtheningProfile `AOF-High-Assurance`. Profile tidak membentuk jenjang Maturity universal.

```text
SchemaValidity != SemanticValidity != AOFConformance
Conformance != Maturity
```

JSON Schema menjadi kontrak struktural kanonis. OpenAPI tidak termasuk dalam jalur rilis kanonis v1.0 LTS. Objek runtime ringkas merupakan proyeksi referensi; pertukaran data dalam bentuk kanonis memerlukan [pemetaan runtime ke kontrak kanonis](reference-implementation/architecture/LTS-A5-RUNTIME-CANONICAL-MAPPING.json) yang terdokumentasi.

## Hasil validasi rilis yang tercatat

[Catatan rilis](release/RELEASE-NOTES.md) dan laporan audit final mencatat hasil berikut untuk baseline yang dirilis:

| Pemeriksaan | Hasil tercatat |
| --- | --- |
| Kesesuaian schema kanonis | 22 / 22 kontrak |
| Kegagalan referensi schema / ketidaksesuaian fixture | 0 / 0 |
| Executable Conformance Suite | 170 test lulus secara reproducible |
| Reference Implementation | 95 test lulus secara reproducible |
| Gate audit LTS | A1–A6 selesai; A5 lulus dengan batasan klaim rilis |
| Release blocker yang diketahui | 0 pada saat deklarasi |

Angka tersebut merupakan hasil validasi rilis yang tercatat, bukan pernyataan bahwa test telah dijalankan ulang pada setiap checkout. Pemeliharaan berikutnya dalam lini v1.0 LTS harus mempertahankan semantik yang dibekukan, kecuali terdapat revisi spesifikasi melalui tata kelola perubahan yang eksplisit.

## Berkontribusi dan keamanan

Kontribusi diterima melalui issue dan pull request. Baca [panduan kontribusi](CONTRIBUTING.md) dan [Code of Conduct](CODE_OF_CONDUCT.md) sebelum mengirim perubahan. Untuk kerentanan, gunakan kanal privat yang dijelaskan dalam [Security Policy](SECURITY.md), bukan public issue.

Pertanyaan penggunaan dan pembahasan komunitas dapat diajukan melalui [GitHub Discussions](https://github.com/aof-framework/aof/discussions). Informasi pemeliharaan repository dan statistik traffic tersedia dalam [panduan maintainer](docs/MAINTAINER-GUIDE.md).

## Lisensi

AOF dilisensikan berdasarkan [Apache License 2.0](LICENSE). Lisensi ini memberikan izin penggunaan, modifikasi, dan distribusi dengan syarat yang tercantum di dalamnya, termasuk explicit patent grant. Nama proyek dan merek tidak otomatis dilisensikan untuk penggunaan di luar ketentuan lisensi.
