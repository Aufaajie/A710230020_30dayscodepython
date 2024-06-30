class Kalkulator:
    def tambah(self, a, b):
        return a + b
    
    def kurang(self, a, b):
        return a - b
    
    def kali(self, a, b):
        return a * b
    
    def bagi(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Tidak bisa dibagi oleh nol!"


calc = Kalkulator()

print("Penjumlahan:", calc.tambah(5, 3))     
print("Pengurangan:", calc.kurang(5, 3))     
print("Perkalian:", calc.kali(5, 3))         
print("Pembagian:", calc.bagi(10, 2))       
print("Pembagian oleh nol:", calc.bagi(5, 0)) 
