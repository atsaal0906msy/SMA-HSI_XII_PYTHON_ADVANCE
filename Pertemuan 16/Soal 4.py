# Latihan 4: Frekuensi Hari
# Tulis program yang membaca file mbox-short.txt. Bangun histogram menggunakan dictionary untuk
# menghitung berapa banyak pesan yang dikirim pada setiap hari dalam seminggu. (Lihat baris yang dimulai
# dengan "From ", kata ketiganya adalah hari). Cetak dictionary hasilnya.

# Membuat dictionary untuk menyimpan jumlah pesan per hari
hari_count = {}

# Membaca file
with open("mbox-short.txt") as file:
    for baris in file:
        # Mengambil hanya baris yang dimulai dengan "From " (dengan spasi)
        if baris.startswith("From "):
            kata = baris.split()
            hari = kata[2]  # kata ke-3 adalah nama hari
            hari_count[hari] = hari_count.get(hari, 0) + 1

# Mencetak hasil
print(hari_count)
