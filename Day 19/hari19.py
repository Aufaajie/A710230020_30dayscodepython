class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku = []

    def tambah_buku(self, buku):
        self.buku.append(buku)
        print(f"Menambahkan buku '{buku.judul}' ke perpustakaan {self.nama}.")

    def hapus_buku(self, buku):
        if buku in self.buku:
            self.buku.remove(buku)
            print(f"Menghapus buku '{buku.judul}' dari perpustakaan {self.nama}.")
        else:
            print(f"Buku '{buku.judul}' tidak ada di perpustakaan {self.nama}.")

    def daftar_buku(self):
        print(f"Buku-buku di perpustakaan {self.nama}:")
        for buku in self.buku:
            print(f"- {buku.judul} oleh {buku.penulis}")

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

def uji_perpustakaan():
    perpus_saya = Perpustakaan("Perpustakaan X")

    buku1 = Buku("Pemrograman Python", "2021")
    buku2 = Buku("Pengantar Kecerdasan Buatan", "2018")

    perpus_saya.tambah_buku(buku1)
    perpus_saya.tambah_buku(buku2)
    perpus_saya.daftar_buku()
    perpus_saya.hapus_buku(buku1)
    perpus_saya.daftar_buku()

uji_perpustakaan()
