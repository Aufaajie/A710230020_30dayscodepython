class Kendaraan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    
    def info(self):
        return f"Kendaraan: {self.nama}, Warna: {self.warna}"

class Mobil(Kendaraan):
    def __init__(self, nama, warna, merek):
        super().__init__(nama, warna)
        self.merek = merek
    
    def info(self):  
        return f"Mobil: {self.nama}, Warna: {self.warna}, Merek: {self.merek}"

class Motor(Kendaraan):
    def __init__(self, nama, warna, jenis):
        super().__init__(nama, warna)
        self.jenis = jenis
    
    def info(self):  
        return f"Motor: {self.nama}, Warna: {self.warna}, Jenis: {self.jenis}"

mobil1 = Mobil("Avanza", "Hitam", "Toyota")
motor1 = Motor("Beat", "Merah", "Honda")

print(mobil1.info())  
print(motor1.info())  
