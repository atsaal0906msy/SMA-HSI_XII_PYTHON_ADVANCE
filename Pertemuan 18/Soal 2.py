# Latihan 2: Class RekeningBank
# Buatlah sebuah class bernama RekeningBank untuk mensimulasikan rekening bank sederhana.
# Buat constructor __init__() yang menerima dua parameter: nomor_rekening dan
# nama_pemilik. Ia juga harus menginisialisasi atribut self.saldo dengan nilai awal 0.
# Buat method lihat_saldo() yang mencetak saldo saat ini.
# Buat method setor(jumlah) yang menambahkan jumlah ke self.saldo dan mencetak pesan
# konfirmasi.
# Buat method tarik(jumlah) yang mengurangi jumlah dari self.saldo. Tambahkan logika if di
# dalamnya: jika jumlah yang ditarik lebih besar dari saldo, cetak pesan "Saldo tidak mencukupi" dan
# jangan ubah saldo. Jika tidak, kurangi saldo dan cetak pesan konfirmasi.
# Buat sebuah objek rekening_budi, lalu coba panggil semua method-nya: setor beberapa kali, tarik,
# dan lihat saldo.

class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0
    def lihat_saldo(self):
        print(f"Sisa saldo saat ini: Rp{self.saldo}")
    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Jumalah setor: Rp{jumlah:,} Berhasil, Saldo saat ini: Rp{self.saldo}")
    def penarikan(self, jumlah):
        if jumlah > self.saldo:
            print("Sorry your money is lose")
        else:
            self.saldo -= jumlah
            print(f"Successful: Rp{jumlah:,} How much money you have: {self.saldo}")

rekening_pace = RekeningBank("6738959726", "paceireng")

rekening_pace.lihat_saldo()
rekening_pace.setor(100000000)
rekening_pace.setor(500000000)  
rekening_pace.penarikan(300000)  
rekening_pace.penarikan(600000)  
rekening_pace.lihat_saldo()

# class RekeningBank:
#     def __init__(self, nomor_rekening, nama_pemilik):
#         self.nomor_rekening = nomor_rekening
#         self.nama_pemilik = nama_pemilik
#         self.saldo = 0

#     def lihat_saldo(self):
#         print(f"Sisa saldo saat ini: Rp{self.saldo}")

#     def setor(self, jumlah):
#         self.saldo += jumlah
#         print(f"Jumlah setor: Rp{jumlah} berhasil, saldo saat ini: Rp{self.saldo}")

#     def tarik(self, jumlah):  # diganti 'tarik' biar konsisten dengan pemanggilan
#         if jumlah > self.saldo:
#             print("Saldo tidak mencukupi untuk penarikan.")
#         else:
#             self.saldo -= jumlah
#             print(f"Berhasil tarik: Rp{jumlah}, saldo tersisa: Rp{self.saldo}")


# # penggunaan
# rekening_pace = RekeningBank("6738959726", "paceireng")

# rekening_pace.lihat_saldo()
# rekening_pace.setor(100000000)
# rekening_pace.setor(500000000)
# rekening_pace.tarik(300000)
# rekening_pace.tarik(600000)
# rekening_pace.lihat_saldo()

