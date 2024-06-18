class Kucing:
    def suara(self):
        print("Meow")

class Anjing:
    def suara(self):
        print("Guk guk")

def main():
    hewan1 = Kucing()
    hewan2 = Anjing()

    for hewan in (hewan1, hewan2):
        hewan.suara()

if __name__ == "__main__":
    main()
