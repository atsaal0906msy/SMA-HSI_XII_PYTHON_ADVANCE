# Latihan 2: Validasi Nomor Telepon Sederhana
# Buat program yang meminta pengguna memasukkan nomor telepon. Program harus memvalidasi apakah
# input tersebut hanya berisi angka dan panjangnya antara 10 sampai 13 digit.
# Gunakan re.search() dengan jangkar ^ dan $.
# Gunakan quantifier + atau yang lebih spesifik.
# Cetak "Format nomor telepon valid." atau "Format tidak valid."
# Pola yang mungkin: ^\d+$ (ini hanya mengecek apakah semuanya digit, kamu perlu menambahkan
# pengecekan panjang dengan len()).

import re

no_telpon = input("Masukan Nomor Telpon: ")

pola = r'^\d+$'

if re.search(pola, no_telpon) and 10 <= len(no_telpon) <= 13:
    print("No telpon valid")
else:
    print("Salah kali No telponya")

