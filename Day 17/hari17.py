class Orang:
    def __init__(self, nama, umur):
        self.nama = nama  
        self.umur = umur  

    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")



if __name__ == "__main__":
    orang1 = Orang("Budi", 25)
    
    orang1.tampilkan_info()

    orang1.umur = 27
    
    orang1.tampilkan_info()
