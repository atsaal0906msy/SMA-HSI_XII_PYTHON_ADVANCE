
try:
    with open("transaksi_kotor.txt", "r", encoding="utf-8") as file_input:
        with open("laporan_bersih.txt", "w", encoding="utf-8") as file_output:
            
            file_output.write("LAPORAN TRANSAKSI BERSIH\n")
            file_output.write("="*25 + "\n\n")

            grand_total = 0 

            
            for baris in file_input:
                baris = baris.strip()
                if not baris:  
                    continue

                
                data_potongan = baris.split(",")

                
                id_bersih = data_potongan[0].strip().upper()
                nama_bersih = data_potongan[1].strip().title()
                jumlah = int(data_potongan[2].strip())
                harga = float(data_potongan[3].strip())

                
                total_harga = jumlah * harga
                grand_total += total_harga

                
                string_output = f"ID: {id_bersih} | Produk: {nama_bersih} | Jumlah: {jumlah} | Total Harga: Rp {total_harga}\n"

                
                file_output.write(string_output)

            
            file_output.write("\n--- ANALISIS SELESAI ---\n")
            file_output.write(f"Grand Total Semua Transaksi: Rp {grand_total}\n")

    print("Proses pembersihan data selesai. Laporan disimpan di laporan_bersih.txt")

except FileNotFoundError:
    print("File transaksi_kotor.txt tidak ditemukan. Pastikan file ada di folder yang sama.")
