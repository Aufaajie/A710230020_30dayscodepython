class Transportasi:
    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis
        self.merk = merk
        self.tahun = tahun
        self.jalankan = False

    def mulai_berjalan(self):
        if not self.jalankan:
            self.jalankan = True
            print(f"{self.merk} {self.jenis} mulai berjalan.")
        else:
            print(f"{self.merk} {self.jenis} sudah berjalan.")

    def berhenti(self):
        if self.jalankan:
            self.jalankan = False
            print(f"{self.merk} {self.jenis} berhenti.")
        else:
            print(f"{self.merk} {self.jenis} sudah berhenti.")

    def status(self):
        if self.jalankan:
            print(f"{self.merk} {self.jenis} sedang berjalan.")
        else:
            print(f"{self.merk} {self.jenis} sedang berhenti.")

if __name__ == "__main__":
    mobil = Transportasi("mobil", "Toyota", 2020)
    motor = Transportasi("motor", "Honda", 2022)

    mobil.mulai_berjalan()
    motor.mulai_berjalan()
    mobil.status()
    motor.status()
    mobil.berhenti()
    motor.berhenti()
    mobil.status()
    motor.status()
