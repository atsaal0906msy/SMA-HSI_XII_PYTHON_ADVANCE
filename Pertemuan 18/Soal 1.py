# Latihan 1: Class Kucing
# Buatlah sebuah class bernama Kucing.
# Buat constructor __init__() yang menerima dua parameter: nama dan warna. Constructor ini
# harus menyimpan nilai-nilai tersebut ke dalam atribut self.nama dan self.warna.
# Buat sebuah method bernama bersuara() yang tidak memiliki parameter (selain self). Ketika
# dipanggil, method ini harus mencetak "Meow!".
# Buat sebuah method bernama perkenalkan_diri() yang mencetak kalimat seperti "Halo, saya
# kucing bernama [nama] dan warna saya [warna].".
# Buat dua object (instance) dari class Kucing dengan nama dan warna yang berbeda (misal, "Oren"
# berwarna "Oranye" dan "Milo" berwarna "Coklat").
# Panggil method perkenalkan_diri() dan bersuara() dari kedua objek tersebut.

class kucing :
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna 
        
    def bersuara(self):
       if self.bersuara:
           print("AAHHH")
    
    def perkenalan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna} dan bisa bersuara.")

kucing_saya = kucing("Pace", "Hitam")

kucing_saya.perkenalan_diri()
kucing_saya.bersuara()

kucing_saya2 = kucing("Jawa", "Hama")

kucing_saya2.perkenalan_diri()
kucing_saya2.bersuara()



# class Kucing:
#     def __init__(self, nama, warna):
#         self.nama = nama
#         self.warna = warna 
        
#     def bersuara(self):
#         return "Kamu idaman banget"   # fungsi ini mengembalikan string
    
#     def perkenalan_diri(self):
#         print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}. "
#               f"Saya bisa mengeluarkan suara {self.bersuara()}.")  # panggil fungsi pakai ()
        

# kucing_saya = Kucing("Pace", "Hitam")
# kucing_saya.perkenalan_diri()
# print(kucing_saya.bersuara())

# kucing_saya2 = Kucing("Jawa", "Hama")
# kucing_saya2.perkenalan_diri()
# print(kucing_saya2.bersuara())

# class Kucing:
#     def __init__(self, nama, warna, suara="AAHHH"):
#         self.nama = nama
#         self.warna = warna 
#         self.bersuara = suara   # jadikan atribut string
    
#     def perkenalan_diri(self):
#         print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}. "
#               f"Saya bisa mengeluarkan suara {self.bersuara}.")
        

# kucing_saya = Kucing("Pace", "Hitam")
# kucing_saya.perkenalan_diri()

# kucing_saya2 = Kucing("Jawa", "Hama", "MIAWW")
# kucing_saya2.perkenalan_diri()

