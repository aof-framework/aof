# Berkontribusi pada AOF

Terima kasih telah membantu mengembangkan AI Orchestration Framework. Bahasa Indonesia digunakan sebagai bahasa utama dokumentasi. Canonical technical terms, formal identifier, nama komponen, state, dan normative keywords tetap ditulis dalam English sesuai spesifikasi.

Dengan mengirimkan kontribusi, Anda menyetujui bahwa kontribusi tersebut dilisensikan berdasarkan [Apache License 2.0](LICENSE), kecuali Anda menyatakannya secara eksplisit sebagai “Not a Contribution”.

## Sebelum membuat perubahan

1. Baca [README](README.md), [spesifikasi](specification/AOF-v1.0-Framework-Specification.md), dan [Code of Conduct](CODE_OF_CONDUCT.md).
2. Cari issue yang sudah ada agar pembahasan tidak terduplikasi.
3. Buat issue terlebih dahulu untuk perubahan `Semantic`, `Security`, `Conformance`, atau `Extension` yang berdampak luas.
4. Jangan melaporkan kerentanan melalui public issue. Ikuti [Security Policy](SECURITY.md).

Setiap perubahan spesifikasi harus diklasifikasikan sebagai `Editorial`, `Clarification`, `Semantic`, `Security`, `Conformance`, atau `Extension`. Lini v1.0 LTS mempertahankan semantik yang telah dibekukan. Perubahan `Semantic` tidak boleh masuk diam-diam sebagai koreksi editorial dan harus mengikuti versioned change control.

## Menyiapkan lingkungan

Gunakan Python 3.11 atau lebih baru:

```bash
python -m venv .venv
```

Aktifkan virtual environment dengan `. .venv/bin/activate` pada shell POSIX atau `.venv\Scripts\Activate.ps1` pada PowerShell, kemudian jalankan:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Jalankan test dari direktori komponennya:

```bash
cd conformance
python -m pytest -q -p no:cacheprovider
cd ../reference-implementation
python -m pytest -q -p no:cacheprovider
```

## Validasi release metadata dan formula

Setelah mengubah berkas repository, perbarui checksum dan jalankan validator:

```bash
python tools/update_checksums.py
python tools/validate_release.py --compare-baseline
```

Untuk perubahan formula, pasang `mathjax-full` 3.2.2 pada direktori sementara dan jalankan validator math. Contoh untuk shell POSIX:

```bash
npm install --prefix /tmp/aof-math-validation --ignore-scripts --no-audit --no-fund mathjax-full@3.2.2
NODE_PATH=/tmp/aof-math-validation/node_modules node tools/validate_math.cjs
```

Jangan memperbarui `release/math-revision/mathjax-validation.json` tanpa benar-benar menjalankan validator yang dicatat di dalam laporan.

## Pull request

Pull request yang baik:

- memiliki scope kecil dan tujuan yang jelas;
- menghubungkan issue terkait;
- menjelaskan klasifikasi perubahan dan dampak semantiknya;
- memperbarui test, dokumentasi, manifest, provenance, dan checksum bila relevan;
- mencantumkan command validasi beserta hasilnya; dan
- tidak menyertakan secret, credential, cache, atau artefak sementara.

Gunakan Conventional Commits bila memungkinkan, misalnya `docs:`, `fix:`, `test:`, `ci:`, atau `chore:`. Maintainer dapat meminta pemisahan perubahan sebelum review atau merge.

## Pelaporan masalah

Gunakan template issue yang paling sesuai. Sertakan versi, Profile, scope, langkah reproduksi, hasil yang diharapkan, hasil aktual, serta Evidence yang aman untuk dipublikasikan. Jangan menyertakan data sensitif atau private chain-of-thought.
