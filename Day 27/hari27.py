class Hewan:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat

    def suara(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan metode ini.")

    def info(self):
        return f"{self.jenis} hidup di {self.habitat}"

class Kucing(Hewan):
    def __init__(self, jenis, habitat, warna, nama):
        super().__init__(jenis, habitat)
        self.warna = warna
        self.nama = nama

    def suara(self):
        return "Meow"

    def info_kucing(self):
        return f"Kucing bernama {self.nama}, berjenis {self.jenis}, berwarna {self.warna}, hidup di {self.habitat}"

    def bermain(self):
        return f"{self.nama} sedang bermain dengan bola benang."

# Contoh penggunaan
hewan1 = Hewan("Mamalia", "Hutan")
print(hewan1.info())

kucing1 = Kucing("Mamalia", "Rumah", "Putih", "Milo")
print(kucing1.info_kucing())
print(kucing1.suara())
print(kucing1.bermain())