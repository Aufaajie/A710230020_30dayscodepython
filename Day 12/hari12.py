class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama  
        self.__nim = nim  
        self.__jurusan = jurusan  
        self.__ipk = 0.0  
    
    @property
    def nama(self):
        return self.__nama
    
    @property
    def nim(self):
        return self.__nim
   
    @property
    def jurusan(self):
        return self.__jurusan
    
    @property
    def ipk(self):
        return self.__ipk
 
    def set_ipk(self, new_ipk):
        if 0.0 <= new_ipk <= 4.0:
            self.__ipk = new_ipk
        else:
            print("Invalid IPK value. IPK should be between 0.0 and 4.0.")

mahasiswa1 = Mahasiswa("Muhammad Aufa Ajie", "A710230020", "PTI")
print(mahasiswa1.nama) 
print(mahasiswa1.nim)   
print(mahasiswa1.jurusan)  
print(mahasiswa1.ipk)   

mahasiswa1.set_ipk(3.5)  
print(mahasiswa1.ipk)   

mahasiswa1.set_ipk(4.5)  
print(mahasiswa1.ipk)   
