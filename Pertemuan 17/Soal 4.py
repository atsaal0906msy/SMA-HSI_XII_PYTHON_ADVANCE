# Latihan 4: Dictionary dengan Tuple Key
# Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
# untuk menyimpan nama bidak catur. Contoh:
# papan_catur[(1, 'a')] = "Benteng Putih"
# papan_catur[(8, 'h')] = "Benteng Hitam"
# Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a').

kalimat = input("Masukkan sebuah kalimat: ")
kalimat = kalimat.lower()
kata_kata = kalimat.split()


histogram = {}
 
for kata in kata_kata:
    if kata in histogram:
        histogram[kata] += 1
    else:
        histogram[kata]
print("Histogram kata:", histogram) 