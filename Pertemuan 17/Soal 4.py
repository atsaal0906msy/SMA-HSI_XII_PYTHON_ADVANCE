# Latihan 4: Dictionary dengan Tuple Key
# Buatlah sebuah dictionary bernama papan_catur. Gunakan tuple (baris, kolom) sebagai key
# untuk menyimpan nama bidak catur. Contoh:
# papan_catur[(1, 'a')] = "Benteng Putih"
# papan_catur[(8, 'h')] = "Benteng Hitam"
# Isi beberapa posisi, lalu akses dan cetak bidak yang ada di posisi (1, 'a').

papan_catur = {}

papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'b')] = "Kuda Putih"
papan_catur[(1, 'c')] = "Gajah Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(8, 'g')] = "Kuda Hitam"

print("Bidak di (1, 'a') adalah:", papan_catur[(1, 'a')])

print("\nIsi papan catur:")
for posisi, bidak in papan_catur.items():
    print(f"Posisi {posisi}: {bidak}")
