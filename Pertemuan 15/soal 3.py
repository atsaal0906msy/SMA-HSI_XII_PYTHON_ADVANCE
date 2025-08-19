# Latihan 3: Penggunaan .get()
# Masih dengan dictionary biodata.
# Coba akses key "pekerjaan" menggunakan bracket notation []. Apa yang terjadi? (Beri komentar
# pada baris ini agar tidak error).
# Sekarang, akses key "pekerjaan" menggunakan metode .get(). Cetak hasilnya.
# Akses lagi key "pekerjaan" menggunakan .get(), tapi kali ini berikan nilai default "Pelajar".
# Cetak hasilnya 

biodata = {
    "nama": "Atsaal",
    "umur": 20,
    "hobi": "Ngoding"
}

print(biodata.get("pekerjaan"))  
print(biodata.get("pekerjaan", "Pelajar"))  
