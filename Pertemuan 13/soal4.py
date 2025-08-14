# Latihan 4: Slicing dan Penggabungan
# Buat dua buah list: awal_minggu = ["Senin", "Selasa", "Rabu"] dan akhir_minggu =
# ["Kamis", "Jumat", "Sabtu", "Minggu"].
# Gunakan operator + untuk menggabungkan keduanya menjadi list baru bernama seminggu.
# Dari list seminggu, gunakan slicing untuk membuat list baru bernama hari_kerja yang hanya
# berisi hari Senin sampai Jumat.
# Cetak list hari_kerja.

awal_minggu = ["Senin", "Selasa", "Rabu"]
akhir_minggu = ["Kamis", "Jumat", "Sabtu", "Minggu"]
seminggu = awal_minggu + akhir_minggu
hari_sibuk = seminggu[:5]
hari_ngangur = seminggu[5:]
print("hari sibuk kerja", hari_sibuk)
print("hari ngangur", hari_ngangur)  
  