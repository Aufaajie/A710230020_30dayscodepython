class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
    
    def tambah(self):
        return self.angka1 + self.angka2
    
    def kurang(self):
        return self.angka1 - self.angka2
    
    def kali(self):
        return self.angka1 * self.angka2
    
    def bagi(self):
        if self.angka2 != 0:
            return self.angka1 / self.angka2
        else:
            return "Error: Pembagian dengan nol tidak diperbolehkan"

def main():
    angka1 = 10
    angka2 = 5

    kalkulator = Kalkulator(angka1, angka2)

    print(f"{angka1} + {angka2} = {kalkulator.tambah()}")
    print(f"{angka1} - {angka2} = {kalkulator.kurang()}")
    print(f"{angka1} * {angka2} = {kalkulator.kali()}")
    print(f"{angka1} / {angka2} = {kalkulator.bagi()}")

if __name__ == "__main__":
    main()
