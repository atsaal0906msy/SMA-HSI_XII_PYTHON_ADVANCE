# Latihan 4: Menemukan Kata dengan Pola
# Diberikan kalimat: kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan.".
# Gunakan re.findall() untuk menemukan semua kata yang diakhiri dengan huruf 'g'.

import re

kalimat = "Kucing, anjing, musang dan burung adalah hewan peliharaan."

hasil = re.findall("\S+g", kalimat)
print(hasil)