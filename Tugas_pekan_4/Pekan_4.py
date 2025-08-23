
import os

SURVEI = [
    {
        "pertanyaan": "Apa makanan kesukaan saya?",
        "opsi": ["Roti", "Pizza", "Donat", "Noodle"]
    },
    {
        "pertanyaan": "Apa mobil impian saya?",
        "opsi": ["Ferrari", "Lamborghini", "McLaren", "Bugatti: Veyron, Chiron."]
    },
    {
        "pertanyaan": "Siapa my wife ketika sudah sukses?",
        "opsi": ["Ustadzah", "Artis ", "Atlet", "Chef"]
    }
]

hasil_polling = {}
for item_survei in SURVEI:
    for opsi in item_survei["opsi"]:
        hasil_polling[opsi] = 0


print("="*44)
print("      SELAMAT DATANG DI APLIKASI POLLING")
print("="*44)

for idx, item_survei in enumerate(SURVEI, start=1):
    print(f"\nPertanyaan {idx}: {item_survei['pertanyaan']}")
    for opsi in item_survei["opsi"]:
        print("  -", opsi)

    
    while True:
        jawaban = input("Jawaban Anda: ")
        if jawaban in item_survei["opsi"]:
            print(">", jawaban)
            print("\n--- Terima kasih! ---")
            hasil_polling[jawaban] += 1
            break
        else:
            print("Jawaban tidak valid. Silakan pilih dari opsi yang tersedia.")


print("\n" + "="*44)
print("             HASIL POLLING")
print("="*44)

total_suara = sum(hasil_polling.values())
for opsi, jumlah in hasil_polling.items():
    if total_suara > 0:
        persen = (jumlah / total_suara) * 100
    else:
        persen = 0
    print(f"{opsi} : {jumlah} suara ({persen:.2f}%)")

print("="*44)


with open("hasil_polling.txt", "w", encoding="utf-8") as f:
    f.write("HASIL POLLING\n")
    f.write("="*30 + "\n")
    for opsi, jumlah in hasil_polling.items():
        persen = (jumlah / total_suara * 100) if total_suara > 0 else 0
        f.write(f"{opsi} : {jumlah} suara ({persen:.2f}%)\n")
