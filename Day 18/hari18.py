def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Hasil pembagian {a} dengan {b} adalah: {result}")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol!")
    except TypeError:
        print("Error: Tipe data yang dimasukkan tidak sesuai")
    except Exception as e:
        print(f"Error: Terjadi kesalahan - {e}")

divide_numbers(10, 2)     
divide_numbers(10, 0)      
divide_numbers(10, '2')    
divide_numbers(10, [])     
