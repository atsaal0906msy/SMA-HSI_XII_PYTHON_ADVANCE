# Latihan 4: Histogram Kata
# Buat program yang:
# Meminta pengguna memasukkan sebuah kalimat.
# Membuat histogram (dalam bentuk dictionary) yang menghitung frekuensi setiap kata (bukan
# huruf) dalam kalimat tersebut.
# Cetak dictionary histogram tersebut.
# Petunjuk: Gunakan metode .split() untuk mengubah kalimat menjadi list kata-kata terlebih
# dahulu. Abaikan huruf besar/kecil dengan mengubah seluruh kalimat menjadi lowercase di awal.

kalimat = input("Masukkan sebuah kalimat: ")
kalimat = kalimat.lower()
kata_list = kalimat.split()

histogram = {}

for kata in kata_list:
    histogram[kata] = histogram.get(kata, 0) + 1
print("Histogram kata:", histogram)
