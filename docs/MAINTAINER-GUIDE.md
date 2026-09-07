# Panduan maintainer repository AOF

Dokumen ini membahas operasi repository GitHub. Tata kelola semantik AOF tetap mengikuti spesifikasi dan versioned change control.

## Traffic dan clone

GitHub menyediakan statistik agregat melalui **Insights → Traffic**. Data mencakup clone, unique cloner, page view, referrer, dan popular content untuk jendela waktu yang disediakan GitHub. GitHub tidak mengungkap identitas pengguna yang melakukan clone.

Gunakan GitHub CLI untuk membaca statistik clone:

```bash
gh api repos/aof-framework/aof/traffic/clones
```

Ringkasan count dan unique cloner:

```bash
gh api repos/aof-framework/aof/traffic/clones --jq '{count, uniques, clones}'
```

Endpoint memerlukan hak push pada repository. Jangan commit token, response mentah yang mengandung metadata internal, atau data traffic tanpa retention policy yang jelas.

## Release download

GitHub menampilkan jumlah download per release asset, bukan identitas pengunduh. Untuk melihat count melalui CLI:

```bash
gh api repos/aof-framework/aof/releases --jq '.[] | {tag_name, assets: [.assets[] | {name, download_count}]}'
```

Clone repository tidak dihitung sebagai release download. Paket pada registry lain memiliki statistiknya sendiri dan tetap umumnya tidak mengungkap identitas pengguna.

## Security and analysis

Pertahankan fitur berikut dalam keadaan aktif:

- Dependabot alerts dan security updates;
- secret scanning dan push protection;
- private vulnerability reporting; dan
- CodeQL melalui workflow repository.

Tinjau hasilnya melalui tab **Security**. Jangan menyalin detail kerentanan yang belum dikoordinasikan ke public issue atau Discussion.

## Release integrity

Sebelum merge yang mengubah berkas release, jalankan:

```bash
python tools/update_checksums.py
python tools/update_checksums.py --check
python tools/validate_release.py --compare-baseline
```

Perubahan formula juga harus menjalankan validator yang dijelaskan dalam [rekaman revisi formula](../release/math-revision/README.md). Checksum aktif merepresentasikan working tree saat ini; checksum historis tetap disimpan sebagai provenance.

## Pengelolaan komunitas

- Gunakan issue untuk bug dan proposal yang dapat dibahas secara publik.
- Gunakan Discussions untuk pertanyaan, ide awal, dan penggunaan AOF.
- Gunakan private vulnerability reporting untuk security report dan laporan Code of Conduct yang sensitif.
- Pastikan perubahan pada area governance dan release ditinjau oleh CODEOWNERS.
