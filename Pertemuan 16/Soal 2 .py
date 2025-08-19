# Latihan 2: Manajemen Kontak
# Buat program manajemen kontak sederhana:
# Buat dictionary kosong bernama kontak.
# Tambahkan tiga kontak (misal: "Ibu", "Ayah", "Teman") beserta nomor teleponnya.
# Ubah nomor telepon "Ibu".
# Gunakan .pop() untuk menghapus "Teman".
# Cetak dictionary kontak akhir

kontak = {}

kontak["Ibu"] = "081234567890"
kontak["Ayah"] = "082345678901"
kontak["Teman"] = "083456789012" 
kontak["Ibu"] = "081111111111"

kontak.pop("Teman")

print("Kontak akhir:", kontak)