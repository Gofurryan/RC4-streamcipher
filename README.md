# 🔏Implementasi RC4 Stream Cipher (Python)

Repositori ini berisi program sederhana yang mendemonstrasikan algoritma kriptografi **RC4 (Rivest Cipher 4)** yang dibangun sepenuhnya dari awal (*from scratch*) menggunakan bahasa pemrograman Python. 

Program ini tidak menggunakan *library* enkripsi instan, melainkan mengimplementasikan langsung logika matematika dan manipulasi *array* yang menjadi inti dari algoritma RC4. Proyek ini sangat cocok untuk tujuan edukasi dan pemahaman cara kerja *Symmetric Stream Cipher*.

## 🔎 Fitur Utama

* **Murni *From Scratch*:** Implementasi manual dari fase KSA (*Key-Scheduling Algorithm*) dan PRGA (*Pseudo-Random Generation Algorithm*).
* **Efisiensi Memori:** Menggunakan fitur *generator* (`yield`) pada Python untuk memproduksi *keystream* secara efisien.
* **Operasi Logika XOR:** Mendemonstrasikan bagaimana satu fungsi yang sama dapat digunakan untuk enkripsi maupun dekripsi.
* **Penanganan *Error* (Error Handling):** Dilengkapi dengan validasi `try...except` untuk menangani kegagalan dekripsi jika pengguna memasukkan kunci yang salah (mencegah *crash* karena `UnicodeDecodeError`).

## 💢 Prasyarat

Program ini ditulis menggunakan fungsi bawaan Python standar. Hanya membutuhkan:
* **Python 3.x** terinstal di sistem Anda.
* Tidak ada *library* eksternal yang perlu diinstal (tidak perlu `pip install`).

## 🎲 Cara Menjalankan Program

Ikuti langkah-langkah berikut untuk menjalankan simulasi enkripsi dan dekripsi RC4 di terminal atau *command prompt* Anda:

1. **Clone repositori ini** ke mesin lokal Anda:
   ```bash
   git clone https://github.com/Gofurryan-RC4-streamcipher.git
   
2. **Masuk ke direktori** tempat file disimpan:
   ```bash
   cd RC4-streamcipher
   
3. **Jalankan Script Python:**
   ```bash
   python rc4.py

## 💥 Output Program

Ketika program dijalankan, Kamu akan melihat simulasi enkripsi teks asli menjadi ciphertext (dalam format Heksadesimal), dan pengembaliannya menjadi teks utuh jika kunci yang digunakan benar:
```bash
=== DEMONSTRASI RC4 ===
Pesan Asli   : Halo, ini pesan rahasia yang dienkripsi dengan RC4!
Kunci        : KunciRahasia321

Ciphertext (Hex) : 1a2b3c4d5e... (nilai acak)
Hasil Dekripsi   : Halo, ini pesan rahasia yang dienkripsi dengan RC4!

[STATUS] Sukses! Pesan utuh.
```
*Jika Anda memodifikasi variabel kunci pada blok dekripsi di dalam kode, program akan mendemonstrasikan penolakan sistem terhadap byte acak dan mencetak status "Gagal Total!".*

## ⚠️ Peringatan (Disclaimer)

**PENTING:** Implementasi RC4 dalam repositori ini dibuat **untuk tujuan edukasi dan demonstrasi**. 

RC4 sendiri saat ini sudah dianggap (*deprecated*) dan rentan terhadap berbagai serangan kriptoanalisis modern (seperti serangan pada protokol WEP dan WPA awal). Selain itu, menulis algoritma kriptografi sendiri (*roll-your-own-crypto*) sangat tidak disarankan untuk penggunaan di lingkungan produksi. 

Jika Anda membutuhkan enkripsi untuk aplikasi di dunia nyata, gunakan *library* standar industri yang sudah diaudit dengan baik, seperti modul `cryptography` di Python, dan gunakan algoritma modern seperti **AES-GCM** atau **ChaCha20**.
