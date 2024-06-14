class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def deskripsi(self):
        nama_lengkap = f"{self.tahun} {self.merk} {self.model}"
        return nama_lengkap.title()

    def baca_odometer(self):
        print(f"Mobil ini telah menempuh jarak {self.odometer} mil.")

    def update_odometer(self, jarak_tempuh):
        if jarak_tempuh >= self.odometer:
            self.odometer = jarak_tempuh
        else:
            print("Anda tidak bisa memutar mundur odometer!")

    def tambah_odometer(self, jarak_tambahan):
        self.odometer += jarak_tambahan


mobil_saya = Mobil('Toyota', 'Camry', 2020)
print(mobil_saya.deskripsi())
mobil_saya.baca_odometer()
mobil_saya.update_odometer(15000)
mobil_saya.baca_odometer()
mobil_saya.tambah_odometer(100)
mobil_saya.baca_odometer()
