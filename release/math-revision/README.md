# Rekaman perbaikan formula AOF v1.0 LTS

**Revisi:** LTS-Editorial-2\
**Klasifikasi:** Editorial / mechanical serialization repair\
**Semantik normatif:** Tidak berubah

Direktori ini menyimpan evidence untuk migrasi formula spesifikasi ke format Markdown yang didukung GitHub.

- `formula-changes.json` mencatat baseline commit, hash sebelum dan sesudah, source line awal, teks sebelum dan sesudah, serta klasifikasi setiap perubahan.
- `mathjax-validation.json` mencatat hasil parsing dan rendering seluruh formula dengan MathJax.
- `github-rendering-validation.json` mencatat pemeriksaan format fenced block melalui endpoint Markdown resmi GitHub.

Ledger menggunakan posisi byte/karakter pada spesifikasi `LTS-Editorial-1` sebagai basis. Validator merekonstruksi spesifikasi `LTS-Editorial-2` dari baseline dan ledger, lalu membandingkannya secara byte-identik dengan berkas aktif. Dengan demikian, perubahan di luar operasi yang tercatat akan menyebabkan validasi gagal.

MathJax lokal digunakan sebagai pemeriksaan sintaks dan rendering SVG. Konfigurasi deployment GitHub dapat berbeda, tetapi fenced code block `math` merupakan format display math yang didokumentasikan GitHub.
