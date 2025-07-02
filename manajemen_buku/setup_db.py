# setup_db.py
import sqlite3
import os

DB_PATH = "data/koleksi.db"

def setup_database():
    print(f"Memeriksa/membuat database di: {DB_PATH}")
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS buku(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            penulis TEXT NOT NULL,
            tahun INTEGER NOT NULL CHECK(tahun > 0),
            genre TEXT,
            halaman INTEGER DEFAULT 0
        );
        """
        print("Membuat tabel 'buku' (jika belum ada)...")
        cursor.execute(sql_create_table)
        conn.commit(); print("-> Tabel 'buku' siap.")
        return True
    except sqlite3.Error as e:
        print(f"-> Error SQLite saat setup: {e}")
        return False
    finally:
        if conn:
            conn.close()
            print("-> Koneksi DB setup ditutup.")

if __name__ == "__main__":
    print("--- Memulai Setup Database Koleksi Buku ---")
    if setup_database():
        print(f"\nSetup database '{os.path.basename(DB_PATH)}' selesai.")
    else:
        print(f"\nSetup database GAGAL.")
    print("--- Setup Database Selesai ---")
