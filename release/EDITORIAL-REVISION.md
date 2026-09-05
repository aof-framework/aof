# Revisi editorial AOF v1.0 LTS

**Release:** v1.0 LTS\
**Status:** RELEASED\
**Tanggal rilis:** 2026-09-05\
**Revisi editorial:** LTS-Editorial-1

Revisi ini menyelaraskan metadata publik dengan deklarasi LTS yang telah selesai. Tanggal rilis tetap; revisi ini bukan rilis semantik baru dan tidak memperpanjang klaim dukungan atau cakupan Conformance.

## Perubahan

- Header spesifikasi dan metadata komponen aktif menyatakan `RELEASED`.
- Status audit aktif mengikuti keputusan final: A4 `PASS`, A5 `PASS_WITH_RELEASE_CLAIM_CONSTRAINT`.
- Appendix G–W dan artefak audit diberi konteks historis. Keputusan lama tetap tersimpan sebagai evidence.
- Manifest aktif membedakan komponen hasil ekstraksi dari ZIP paket asli yang tidak tersedia.
- Checksum aktif mencakup berkas saat ini; manifest dan checksum asli disimpan byte-for-byte dalam [arsip provenance](provenance/original-v1.0-LTS/README.md).

## Batas semantik dan provenance

Requirement, Invariant, formula, identifier, Profile, schema, fixture, dan kode runtime tidak diubah. Pada spesifikasi, perubahan terbatas pada header rilis dan penambahan penanda konteks historis.

- Commit sebelum revisi: `1dd6738fdcd106750194a16666136402917cd2e8`.
- SHA-256 spesifikasi baseline asli: `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`.
- SHA-256 spesifikasi revisi editorial: `bc83ce35231460283348105744ae82d7ed87662e37923985959a1781eb6b3d17`.

Hash lama dalam provenance schema, test, dan laporan audit tetap mengidentifikasi sumber saat artefak tersebut dibuat. Field `current_specification` pada manifest komponen menunjuk revisi editorial sekarang. Perbedaan hash mencerminkan perubahan teks metadata; hasil audit historis tidak ditulis ulang sebagai hasil audit baru.

## Verifikasi checksum

Jalankan `python tools/validate_release.py` dari root repository. Checksum dihitung atas byte berkas. Aturan `.gitattributes` menjaga line ending berkas terdaftar agar hasil konsisten setelah checkout. Checksum root tidak mencakup dirinya sendiri; checksum komponen menggunakan path relatif terhadap direktori komponennya. Tidak ada ZIP yang diklaim telah diverifikasi jika tidak tersedia.

Pemeriksaan ini memvalidasi metadata dan integritas berkas, bukan sertifikasi Conformance baru. Angka 170 dan 95 dalam catatan rilis merupakan hasil audit rilis asli.

## Validasi revisi editorial

Pengujian ulang menggunakan Python dan pytest 9.1.1 menghasilkan **170 test lulus** pada Conformance Suite dan **95 test lulus** pada Reference Implementation. Kedua suite dijalankan dari direktori komponennya dengan `python -m pytest -q -p no:cacheprovider`.

Pemeriksaan `python tools/validate_release.py --compare-baseline` memverifikasi metadata aktif, JSON, target tautan lokal, checksum, perubahan spesifikasi yang hanya bersifat editorial, serta kesamaan byte arsip metadata asli. Opsi `--compare-baseline` memerlukan riwayat Git pada commit baseline yang disebutkan di atas.
