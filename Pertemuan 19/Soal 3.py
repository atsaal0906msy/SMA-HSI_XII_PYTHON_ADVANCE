# Latihan 3: re.search() vs. re.findall()
# Diberikan string teks = "python adalah bahasa yang menyenangkan, python mudah
# dipelajari.".
# Gunakan re.search('python', teks). Apa yang dikembalikannya? Cetak .group()-nya.
# Gunakan re.findall('python', teks). Apa yang dikembalikannya? Cetak hasilnya.
# Jelaskan perbedaan output keduanya.

import re

teks = "Python adalah bahasa yang menyenangkan, python mudah dipelajari."

hasil_search = re.search('python', teks)
if hasil_search:
    print("Hasil re.search():", hasil_search.group())
else:
    print("Tidak ditemukan.")

hasil_findall = re.findall('python', teks)
print("Hasil re.findall():", hasil_findall)
