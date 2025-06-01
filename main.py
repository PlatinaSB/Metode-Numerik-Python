from utils import get_float_optional, get_int_optional


def main():
    print("""
=======================================
PENCARI AKAR FUNGSI NUMERIK
=======================================

Metode Tertutup
1. Bagi Dua (Bisection)
2. Regula Falsi

Metode Terbuka
3. Iterasi Titik Tetap
4. Newton-Raphson
5. Secant
           """)

    while True:
        try:
            metode_pilihan = int(input("Pilih metode (1-5): "))
            if 1 <= metode_pilihan <= 5:
                break
            else:
                print("Pilihan metode tidak valid. Harap masukkan angka antara 1 dan 5.")
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat.")
    
    print("Fungsi matematika yang didukung: sin, cos, tan, exp, log, sqrt, abs, pow, pi, e, pow, arcsin, arccos, arctan")
    print("Referensi operator Python: https://www.w3schools.com/python/python_operators.asp")

    if metode_pilihan == 1:
        NotImplementedError

    if metode_pilihan == 2:
        NotImplementedError

    if metode_pilihan == 3:
        NotImplementedError

    if metode_pilihan == 4:
        NotImplementedError

    if metode_pilihan == 5:
        NotImplementedError

            
if __name__ == "__main__":
    L = 0
    while L!=1:
        main()
        p = input("\nlanjut? Y/n : ")
        if p == "y" or p == "Y":
            L = 0
        if p == "n" or p == "N":
            L = 1