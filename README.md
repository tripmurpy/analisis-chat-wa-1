<div align="center">
  <h1>📊 Analisis Chat WhatsApp dengan Python</h1>
  <p><i>Proyek Data Analyst untuk mengekstrak, membersihkan, dan menganalisis data riwayat obrolan WhatsApp.</i></p>
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
  ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
</div>

---

## 🚀 Tentang Proyek

Pernahkah kamu penasaran siapa yang paling sering memulai percakapan di pagi hari? Atau bulan apa obrolan kalian paling aktif? 🤔 

Proyek **Analisis Chat WhatsApp** ini dibuat untuk menjawab pertanyaan-pertanyaan tersebut! Dengan memanfaatkan kekuatan **Python** dan **Pandas**, proyek ini secara otomatis mengubah file mentah `WhatsApp Chat.txt` (yang terlihat berantakan) menjadi format terstruktur berbentuk tabel `.csv` yang siap dianalisis secara mendalam.

## � Privasi Data

**Penting:** Demi menjaga privasi, **seluruh data obrolan WhatsApp asli** (`.txt`) maupun **data yang telah dibersihkan** (`.csv`) **TIDAK DISERTAKAN** di dalam repositori ini. 
Jika kamu melihat repositori ini kosong dari dataset, hal tersebut disengaja! File bernama `.gitignore` telah dikonfigurasi untuk mengabaikan direktori `chat/`, `data/`, serta semua jenis file teks dan data agar obrolan personal tetap aman.

## �📂 Struktur Direktori

Berikut adalah kerangka dari proyek ini:

```text
📦 analisis-chat
 ┣ 📂 chat                 # Tempat menaruh file mentah (WhatsApp Chat.txt)
 ┣ 📂 data                 # Tempat menyimpan hasil ekstraksi (clean_chat.csv)
 ┣ 📂 starter
 ┃ ┗ 📜 starter.py         # Script utama pengubah .TXT (Regex) ke .CSV
 ┣ 📂 analyst
 ┃ ┣ 📜 no1.py             # Script analisis dasar (misal: filter bulan Januari)
 ┃ ┣ 📜 playground.py      # Script eksperimen pandas dataframe
 ┃ ┗ 📓 playground.ipynb   # Jupyter Notebook untuk visualisasi & analisis lanjutan
 ┗ 📂 venv                 # Virtual Environment Python
```

## ✨ Fitur Utama

- **Regex Parser**: Mengekstrak data penting seperti Tanggal, Jam, Nama Pengirim, dan Isi Pesan secara presisi melalui `starter.py`.
- **Data Cleansing**: Membersihkan <i>noise</i> dari file mentah sehingga dataset aman digunakan.
- **Time-Series Analysis**: Menggunakan `pd.to_datetime()` untuk membedah data berdasarkan waktu (Jam aktif, Bulan spesifik seperti Januari, dsb).
- **Fleksibilitas Analisis**: Menyediakan interaksi langsung via `playground.ipynb` untuk Data Enthusiast yang suka bereksperimen.

## 🛠️ Prasyarat (Requirements)

Sebelum dapat menjalankan proyek ini, pastikan kamu telah menginstall:
- Python (Versi 3.8 ke atas)
- Library `pandas`

Install *dependencies* dengan menjalankan:
```bash
pip install pandas
```

## 👣 Cara Penggunaan

Ikuti langkah-langkah mudah di bawah ini untuk memulai:

1. **Siapkan Data Mentah**  
   Export chat WhatsApp kamu (tanpa media) dan letakkan di dalam folder `chat/` dengan nama file `WhatsApp Chat.txt`.
   
2. **Jalankan Script Pembersih Data**  
   Jalankan file `starter.py` untuk mem-parsing file teks menjadi dataset tabel.
   ```bash
   python starter/starter.py
   ```
   *Output akan menghasilkan file baru bernama `clean_chat.csv` yang nantinya disimpan di folder data atau root proyek sesuai path.*

3. **Mulai Lakukan Analisis!**  
   Gunakan file di dalam folder `analyst/` untuk menjawab pertanyaan analitik kamu.
   Kamu bisa membuka `playground.ipynb` untuk interaksi berbasis Notebook, atau menjalankan:
   ```bash
   python analyst/no1.py
   ```

## 🎯 Ide Analisis Menarik di Proyek Ini

Beberapa studi kasus ("<i>use case</i>") yang telah atau sedang dieksplor dalam folder `analyst`:
- **Early Bird**: Siapa yang secara statistik paling sering mengirim pesan pertama kali di rentang subuh dan pagi hari (04.00 - 07.00)?
- **Monthly Activity**: Bagaimana tren komunikasi di bulan Januari vs Februari?

---

<div align="center">
  Dibuat dengan 💻 dan ☕ oleh Data Enthusiast.
</div>
