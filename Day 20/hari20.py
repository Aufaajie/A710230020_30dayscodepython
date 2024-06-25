class Sekolah:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.daftar_siswa = []

    def tambah_siswa(self, nama_siswa):
        self.daftar_siswa.append(nama_siswa)

    def info_sekolah(self):
        print(f"Sekolah: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print("Daftar Siswa:")
        for siswa in self.daftar_siswa:
            print(f"- {siswa}")


class SMP(Sekolah):
    def __init__(self, nama, alamat, jml_kelas):
        super().__init__(nama, alamat)
        self.jml_kelas = jml_kelas

    def info_sekolah(self):
        super().info_sekolah()
        print(f"Jumlah Kelas: {self.jml_kelas}")


if __name__ == "__main__":
    smp1 = SMP("SMP Negeri 1", "Jl. Raya No. 10", 15)

    smp1.tambah_siswa("Ani")
    smp1.tambah_siswa("Budi")
    smp1.tambah_siswa("Cindy")

    smp1.info_sekolah()
