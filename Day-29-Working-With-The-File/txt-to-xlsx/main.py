import pandas as pd

# Baca file teks ke dalam DataFrame
dataframe = pd.read_csv('data.txt', delimiter=', ')  # delimiter disesuaikan dengan pemisah dalam file teks

# Simpan DataFrame ke dalam file Excel
dataframe.to_excel('output.xlsx', index=False)  # index=False untuk mengabaikan indeks baris saat menyimpan

print("File berhasil dikonversi ke Excel.")
