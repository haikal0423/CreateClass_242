class PersegiPanjang:
    def __init__(self, Panjang, Lebar):
        self.panjang = Panjang
        self.lebar = Lebar
    
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    

    def main():
        try:
            panjang = float(input("Masukan Panjang (cm): "))
            lebar = float(input("Masukan lebar (cm): "))

            Persegi_Panjang = PersegiPanjang(panjang, lebar)
            print(Persegi_Panjang)
            if panjang <= 0 or lebar <= 0:
                print("Nilai tidak boleh negatif atau 0")
                return

            elif panjang > 0 and lebar > 0:
                print(f"Keliling: {Persegi_Panjang.hitung_keliling()}cm²")
                print(f"Luas: {Persegi_Panjang.hitung_luas()}cm²")
            else:
                print("Angka harus lebih dari 0!")
        except ValueError:
            print("Masukkan nilai numerik untuk panjang dan lebar.")
            
if __name__== "__main__":
    PersegiPanjang.main()