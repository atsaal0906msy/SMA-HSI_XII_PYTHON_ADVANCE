# Latihan 2: Immutability
# Diberikan tuple koordinat_awal = (10, 20). Tulis kode yang menghasilkan tuple baru bernama
# koordinat_baru yang nilainya (10, 25). Kamu tidak boleh mengubah koordinat_awal secara
# langsung.

angka_awal = (10,20)
angka_baru = angka_awal[0:1] + (25,)

print(angka_baru)

  