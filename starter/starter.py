import pandas as pd
import re

# 1. Menyiapkan pola (Pattern) pembaca teks
# Pola ini mencari: (Tanggal), (Jam) - (Nama Pengirim): (Isi Pesan)
pola = r'^(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}\s?[AP]M)\s-\s(.*?):\s(.*)$'

# Menyiapkan tempat kosong untuk menyimpan data yang sudah rapi
data_bersih = []

# 2. Membaca file txt (Ganti nama file sesuai lokasi file kamu)
lokasi_file = 'chat/WhatsApp Chat.txt'

with open(lokasi_file, 'r', encoding='utf-8') as file:
    for baris in file:
        # Mesin Regex mencoba mencocokkan baris dengan pola
        cocok = re.match(pola, baris)
        
        if cocok:
            # Kalau cocok, masukkan ke tempat penyimpanan
            tanggal = cocok.group(1)
            jam = cocok.group(2)
            pengirim = cocok.group(3)
            pesan = cocok.group(4)
            data_bersih.append([tanggal, jam, pengirim, pesan])

# 3. Mengubah kumpulan data menjadi Tabel (DataFrame) menggunakan Pandas
df = pd.DataFrame(data_bersih, columns=['Tanggal', 'Jam', 'Pengirim', 'Pesan'])

# 4. Menyimpan tabel menjadi file CSV yang rapi!
df.to_csv('clean_chat.csv', index=False)
print("Selamat! File CSV sudah berhasil dibuat dan siap dianalisis!")