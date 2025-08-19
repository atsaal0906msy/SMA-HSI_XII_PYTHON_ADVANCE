# Latihan 2: Modifikasi Dictionary
# Gunakan dictionary biodata dari Latihan 1.
# Tambahkan pasangan key-value baru: "kota": "Nama Kotamu".
# Ubah value dari key "umur" menjadi umurmu tahun depan.
# Cetak dictionary yang sudah diperbarui.


biodata = {
    "nama": "atsaal",
    "umur": 18,
    "hobi": ['Mancing','Ngaji','Lari'],
    "sudah_menikah": True
}

# menambahkan key-value baru
biodata["kota"] = "Cirebon" 
# mengganti key-value
biodata["umur"] = 18
print("Profil setelah ditambah:", biodata)