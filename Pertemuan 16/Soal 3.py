# Latihan 3: Nested Dictionary
# Buatlah sebuah nested dictionary untuk menyimpan data dua produk di sebuah toko online.
# Key utamanya adalah ID produk (misal: "PROD001", "PROD002").
# Setiap produk harus memiliki key untuk "nama", "harga", dan "stok".
# Setelah membuatnya, tulis kode untuk mencetak nama dan harga dari produk dengan ID "PROD002".

# Membuat nested dictionary
produk = {
    "PROD001": {
        "nama": "Laptop Gaming",
        "harga": 15000000,
        "stok": 5
    },
    "PROD002": {
        "nama": "Smartphone",
        "harga": 3500000,
        "stok": 10
    }
}

# Mencetak nama dan harga produk dengan ID PROD002
print("Nama Produk:", produk["PROD002"]["nama"])
print("Harga:", produk["PROD002"]["harga"])
