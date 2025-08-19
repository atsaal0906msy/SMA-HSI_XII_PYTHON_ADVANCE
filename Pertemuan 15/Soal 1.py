# Latihan 1: Membuat dan Mengakses
# Buat sebuah dictionary bernama biodata untuk merepresentasikan dirimu. Isinya harus memiliki
# key: "nama", "umur", "hobi" (hobi bisa berupa list dari beberapa string), dan
# "sudah_menikah" (berisi boolean).
# Cetak seluruh dictionary.
# Cetak hanya value dari key "nama".
# Cetak hobi pertamamu dari list hobi

# Membuat dictionary data siswa

biodata = {
 "nama": "Muhammad Atsaal",
 "umur": 18,
 "hobi": ["Bohong", "Omong Kosong" , "Nyakitin"],
 "sudah_menikah": False,
}


nama_suuu = biodata["nama"]
print(f"Nama saya adalah: {nama_suuu}") 
 
umur_suuu = biodata["umur"]
print(f"Umurnya adalah: {umur_suuu} tahun") 

hobi = biodata["hobi"]
print(f"Umurnya adalah: {hobi}") 

menikah = biodata["sudah_menikah"]
print(f"Sudah Nikah: {menikah} ")