from model import Buku, BukuDigital, BukuFisik
import pandas as pd
import database

class KoleksiBuku:
    def tambah_buku(self, buku: Buku):
        sql = "INSERT INTO buku (judul, penulis, tahun, genre, halaman, tipe) VALUES (?, ?, ?, ?, ?, ?)"
        params = (buku.judul, buku.penulis, buku.tahun, buku.genre, buku.halaman, buku.tipe)
        return database.execute_query(sql, params)

    def semua_buku(self):
        sql = "SELECT * FROM buku ORDER BY tahun DESC"
        rows = database.fetch_query(sql)
        daftar_buku = []
    
        for row in rows:
            tipe = row['tipe']
            if tipe == "Digital":
                buku = BukuDigital(row['judul'], row['penulis'], row['tahun'],
                                   row['genre'], row['halaman'], row['id'])
            else:
                buku = BukuFisik(row['judul'], row['penulis'], row['tahun'],
                                 row['genre'], row['halaman'], row['id'])
            daftar_buku.append(buku)
    
        return daftar_buku

    def hapus_buku(self, id_buku):
        sql = "DELETE FROM buku WHERE id = ?"
        return database.execute_query(sql, (id_buku,))

    def ringkasan_per_genre(self):
        sql = "SELECT genre, COUNT(*) AS jumlah FROM buku GROUP BY genre"
        return database.fetch_query(sql)
    
    def get_dataframe_buku(self) -> pd.DataFrame:
        sql = "SELECT id, judul, penulis, tahun, genre, halaman AS jml_halaman FROM buku ORDER BY tahun DESC"
        return database.get_dataframe(sql)

