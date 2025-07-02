# model.py
class Buku:
    def __init__(self, judul, penulis, tahun, genre, halaman, id_buku=None, tipe="Fisik"):
        self.id = id_buku
        self.judul = str(judul)
        self.penulis = str(penulis)
        self.tahun = str(tahun)
        self.genre = str(genre)
        self.halaman = int(halaman)
        self.tipe = tipe 

    def cetak_info(self):
        return f"{self.judul} ({self.tahun}) oleh {self.penulis}"

class BukuDigital(Buku):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tipe="Digital")

    def cetak_info(self):
        return f"[Digital] {self.judul} ({self.tahun}) - {self.genre}"

class BukuFisik(Buku):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, tipe="Fisik")

    def cetak_info(self):
        return f"[Fisik] {self.judul} ({self.tahun}) - {self.genre}"

