# Latihan 3: Traversing dan Modifikasi
# Buat sebuah list berisi angka: nilai_mentah = [55, 63, 72, 81, 90].
# Buatlah sebuah for loop yang menggunakan range(len(nilai_mentah)) untuk mengunjungi
# setiap elemen.
# Di dalam loop, tambahkan 5 poin ke setiap nilai sebagai "nilai bonus".
# Setelah loop selesai, cetak list nilai_mentah yang sudah berisi nilai-nilai baru.

nilai_mentah = [55, 63, 72, 81, 90]

for i in range(len(nilai_mentah)):
    nilai_mentah[i] += 5 

print("Nilai- nilai baru:", nilai_mentah)   
