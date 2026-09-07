# Security Policy

## Versi yang didukung

| Versi | Dukungan keamanan |
| --- | --- |
| v1.0 LTS | Didukung |
| RC dan versi pra-rilis | Tidak didukung |

## Melaporkan kerentanan

Laporkan kerentanan secara privat melalui [GitHub Private Vulnerability Reporting](https://github.com/aof-framework/aof/security/advisories/new). Jangan membuka public issue untuk kerentanan yang belum dikoordinasikan.

Sertakan informasi berikut bila tersedia:

- komponen, versi, Profile, dan scope yang terdampak;
- langkah reproduksi atau proof of concept yang aman;
- dampak terhadap `Authority`, `Policy`, `Risk`, `State`, `Evidence`, `Verification`, atau Effect Boundary;
- kondisi eksploitasi dan mitigasi sementara; serta
- apakah laporan atau detailnya boleh diatribusikan kepada pelapor.

Jangan mengirim credential, secret produksi, data pribadi, atau private chain-of-thought. Gunakan data uji minimal dan redaksi bagian sensitif.

Maintainer menargetkan konfirmasi penerimaan awal dalam 7 hari kalender dan pembaruan status dalam 14 hari kalender. Waktu perbaikan bergantung pada severity, kompleksitas, dan kebutuhan koordinasi. Publikasi dilakukan setelah mitigasi tersedia atau melalui coordinated disclosure yang disepakati.

## Scope keamanan

Laporan yang relevan mencakup implementasi referensi, schema, Conformance Suite, atau ambiguity spesifikasi yang dapat menyebabkan bypass kontrol. Temuan tentang sistem pihak ketiga atau deployment yang tidak disebabkan oleh AOF berada di luar scope repository ini, tetapi laporan yang menunjukkan kelemahan pada integrasi AOF tetap dapat ditinjau.

Security report tidak otomatis mengubah semantik normatif. Perubahan yang diperlukan mengikuti klasifikasi dan versioned change control AOF.
