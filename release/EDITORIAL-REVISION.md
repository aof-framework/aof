# Revisi editorial AOF v1.0 LTS

**Release:** v1.0 LTS\
**Status:** RELEASED\
**Tanggal rilis:** 2026-09-05\
**Revisi editorial saat ini:** LTS-Editorial-2

Revisi editorial tidak mengubah tanggal rilis, tidak menjadi rilis semantik baru, serta tidak memperpanjang klaim dukungan atau cakupan Conformance.

## LTS-Editorial-2 — kompatibilitas formula GitHub

Revisi ini mengonversi 985 display formula dari delimiter `\[ ... \]` ke fenced code block `math` yang didukung GitHub. Perbaikan mekanis mencakup:

- satu formula tanpa delimiter penutup;
- satu interval waktu dengan delimiter bersarang;
- `\subset eq` dan `\supset eq` menjadi `\subseteq` dan `\supseteq`;
- subscript, superscript, operator perbandingan, dan kurung himpunan yang ter-escape atau tidak terlihat;
- command LaTeX yang menyatu dengan identifier;
- canonical identifier menjadi upright text melalui `\mathrm{...}`;
- satu heading yang masih ter-escape; dan
- pemenggalan satu formula panjang tanpa mengubah urutan sukunya.

Pemetaan lengkap sebelum–sesudah tersedia di [formula-changes.json](math-revision/formula-changes.json). [Laporan MathJax](math-revision/mathjax-validation.json) mencatat bahwa seluruh 985 formula berhasil diparse dan dirender menggunakan `mathjax-full` 3.2.2 dengan package `base` dan `ams`. Pemeriksaan visual dilakukan pada sampel formula sederhana, himpunan, subscript, optimisasi, percabangan `cases`, formula panjang, serta formula yang sebelumnya kehilangan delimiter. Endpoint Markdown resmi GitHub juga merender sampel fenced block sebagai elemen `math-renderer` dengan display math.

## LTS-Editorial-1 — konsistensi metadata

- Header spesifikasi dan metadata komponen aktif menyatakan `RELEASED`.
- Status audit aktif mengikuti keputusan final: A4 `PASS`, A5 `PASS_WITH_RELEASE_CLAIM_CONSTRAINT`.
- Appendix G–W dan artefak audit diberi konteks historis. Keputusan lama tetap tersimpan sebagai evidence.
- Manifest aktif membedakan komponen hasil ekstraksi dari ZIP paket asli yang tidak tersedia.
- Checksum aktif mencakup berkas saat ini; manifest dan checksum asli disimpan byte-for-byte dalam [arsip provenance](provenance/original-v1.0-LTS/README.md).

## Batas semantik dan provenance

Pada `LTS-Editorial-1`, Requirement, Invariant, formula, identifier, Profile, schema, fixture, dan kode runtime tidak diubah. Perubahan terbatas pada header rilis dan penambahan penanda konteks historis. Pada `LTS-Editorial-2`, serialisasi formula diperbaiki berdasarkan notasi serta konteks normatif yang sudah ada; tidak ada Requirement, Invariant, identifier, atau urutan operasional yang ditambah, dihapus, diperkuat, maupun dilemahkan.

- Commit sebelum revisi: `1dd6738fdcd106750194a16666136402917cd2e8`.
- SHA-256 spesifikasi baseline asli: `57ddbd64671eea615535b20f109064d96fb262e781969ef757a6f4d5efa869d5`.
- SHA-256 spesifikasi `LTS-Editorial-1`: `bc83ce35231460283348105744ae82d7ed87662e37923985959a1781eb6b3d17`.
- SHA-256 spesifikasi `LTS-Editorial-2`: `6197f71416984cca1811d5cd0cdd30327cccb9026acc5b92509f8f2a3a137974`.

Hash lama dalam provenance schema, test, dan laporan audit tetap mengidentifikasi sumber saat artefak tersebut dibuat. Field `current_specification` pada manifest komponen menunjuk revisi editorial sekarang. Perbedaan hash mencerminkan perubahan teks metadata; hasil audit historis tidak ditulis ulang sebagai hasil audit baru.

## Verifikasi checksum

Jalankan `python tools/validate_release.py --compare-baseline` dari root repository untuk memeriksa metadata, checksum, dan ledger perubahan. Untuk validasi formula, pasang `mathjax-full` 3.2.2 di luar repository, atur `NODE_PATH`, lalu jalankan `node tools/validate_math.cjs --report release/math-revision/mathjax-validation.json`.

Checksum dihitung atas byte berkas. Aturan `.gitattributes` menjaga line ending berkas terdaftar agar hasil konsisten setelah checkout. Checksum root tidak mencakup dirinya sendiri; checksum komponen menggunakan path relatif terhadap direktori komponennya. Tidak ada ZIP yang diklaim telah diverifikasi jika tidak tersedia.

Pemeriksaan ini memvalidasi metadata dan integritas berkas, bukan sertifikasi Conformance baru. Angka 170 dan 95 dalam catatan rilis merupakan hasil audit rilis asli.

## Validasi revisi editorial

Pengujian ulang menggunakan Python dan pytest 9.1.1 menghasilkan **170 test lulus** pada Conformance Suite dan **95 test lulus** pada Reference Implementation. Kedua suite dijalankan dari direktori komponennya dengan `python -m pytest -q -p no:cacheprovider`.

Pemeriksaan `python tools/validate_release.py --compare-baseline` memverifikasi metadata aktif, JSON, target tautan lokal, checksum, perubahan spesifikasi berdasarkan ledger editorial, serta kesamaan byte arsip metadata asli. Opsi `--compare-baseline` memerlukan riwayat Git pada commit baseline yang disebutkan di atas.
