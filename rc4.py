def ksa(key: bytes) -> list:
    """"
    Key-Scheduling Algorithm (KSA).
    Tahap pertama RC4: Menginisialisasi array S dari 0-255, lalu mengacaknya
    berdasarkan kunci rahasia (key) yang diberikan.
    """
    # Buat array S berisi angka 0 hingga 255 berurutan
    S = list(range(256))
    j = 0
    
    # Acak array S menggunakan kunci
    for i in range(256):
        # Operasi penentuan indeks j yang baru
        j = (j + S[i] + key[i % len(key)]) % 256
        # Tukar (swap) posisi nilai pada S[i] dan S[j]
        S[i], S[j] = S[j], S[i]
        
    return S

def prga(S: list):
    """
    Pseudo-Random Generation Algorithm (PRGA).
    Tahap kedua RC4: Menghasilkan aliran angka acak (keystream) terus-menerus
    berdasarkan array S yang sudah diacak oleh KSA.
    Menggunakan teknik 'yield' (generator) agar efisien memori.
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        
        # Tukar lagi posisinya untuk menambah keacakan seiring waktu
        S[i], S[j] = S[j], S[i]
        
        # Ambil nilai keystream K
        K = S[(S[i] + S[j]) % 256]
        yield K

def rc4(key: str, data: bytes) -> bytes:
    """
    Fungsi utama untuk Enkripsi maupun Dekripsi.
    Karena RC4 adalah Stream Cipher dan beroperasi dengan gerbang logika XOR,
    fungsi enkripsi dan dekripsinya persis sama. (A XOR B = C, C XOR B = A).
    """
    # Ubah string kunci menjadi format byte
    key_bytes = key.encode('utf-8')
    
    # 1. Jalankan KSA untuk mengacak state awal
    S = ksa(key_bytes)
    
    # 2. Siapkan PRGA untuk menghasilkan keystream
    keystream = prga(S)
    
    result = bytearray()
    
    # 3. Proses XOR data asli dengan keystream byte demi byte
    for byte in data:
        result.append(byte ^ next(keystream))
        
    return bytes(result)

# ==========================================
# CONTOH PENGGUNAAN (MAIN PROGRAM)
# ==========================================
if __name__ == '__main__':
    # 1. Siapkan Kunci dan Pesan (Plaintext)
    kunci_rahasia = "Rahasia321"
    pesan_asli = "Halo, ini adalah pesan rahasia yang dienkripsi dengan RC4!"
    
    print("=== DEMONSTRASI RC4 ===")
    print(f"Pesan Asli   : {pesan_asli}")
    print(f"Kunci        : {kunci_rahasia}\n")
    
    # 2. ENKRIPSI
    # Ubah string pesan menjadi bytes sebelum dienkripsi
    data_bytes = pesan_asli.encode('utf-8')
    hasil_enkripsi = rc4(kunci_rahasia, data_bytes)
    
    # Tampilkan dalam format Hexadecimal (karena hasil enkripsi biasanya
    # bukan karakter ASCII yang bisa dibaca/diprint secara normal)
    print(f"Ciphertext (Hex) : {hasil_enkripsi.hex()}")
    
   # 3. DEKRIPSI (Eksperimen dengan kunci yang salah)
    kunci_eksperimen = kunci_rahasia
    hasil_dekripsi_bytes = rc4(kunci_eksperimen, hasil_enkripsi)
    
    print(f"Mencoba dekripsi dengan kunci: {kunci_eksperimen}")

    # 4. Validasi Keberhasilan & Penanganan Error
    try:
        # Coba ubah bytes menjadi string
        pesan_kembali = hasil_dekripsi_bytes.decode('utf-8')
        print(f"Hasil Dekripsi   : {pesan_kembali}")
        
        if pesan_asli == pesan_kembali:
            print("\n[STATUS] Sukses! Pesan utuh.")
        else:
            print("\n[STATUS] Gagal! Pesan berubah.")
            
    except UnicodeDecodeError:
        # Menangkap error jika hasil dekripsi adalah byte acak (bukan teks valid)
        print("\n[STATUS] Gagal Total! Kunci salah.")
        print("Sistem memunculkan UnicodeDecodeError karena hasil dekripsi berupa byte acak yang tidak bisa dibaca sebagai teks.")