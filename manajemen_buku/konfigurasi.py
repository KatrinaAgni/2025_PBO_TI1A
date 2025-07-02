# konfigurasi.py
import os

# Tentukan direktori saat ini (lokasi file ini)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Nama file database
NAMA_DB = "koleksi.db"

# Path lengkap ke file database
DB_PATH = os.path.join(BASE_DIR, "data", NAMA_DB)

# Daftar genre buku
DAFTAR_GENRE = [
    "Fiksi", "Non-Fiksi", "Biografi", "Sejarah", "Teknologi",
    "Pendidikan", "Sastra", "Komik", "Lainnya"
]
