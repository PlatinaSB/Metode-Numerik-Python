from utils import get_float_optional, get_int_optional
from bisection import bisection
from regula_falsi import regula_falsi
from fixed_point import fixed_point
from newton_raphson import newton_raphson




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

    tol = get_float_optional("Masukkan toleransi (default 1e-6): ", 1e-6)
    maxiter = get_int_optional("Masukkan maksimum iterasi (default 100): ", 100)
    
    print("Fungsi matematika yang didukung: sin, cos, tan, exp, log, sqrt, abs, pow, pi, e, pow, arcsin, arccos, arctan")
    print("Referensi operator Python: https://www.w3schools.com/python/python_operators.asp")

    if metode_pilihan == 1:
        expresion_func = input("Masukkan Ekspresi f(x) (contoh: 'x**3 - x - 2'): ")
        a = float(input("Masukkan Nilai a: "))
        b = float(input("Masukkan Nilai b: "))
        root = bisection(expresion_func, a, b, tol, maxiter)
        if root is not None:
            print(f"\nAkar (Metode Bagi Dua): {root:.6f}")
        else:
            print("\nMetode Bagi Dua tidak konvergen atau gagal.")

    if metode_pilihan == 2:
        expresion_func = input("Masukkan Ekspresi f(x) (contoh: 'x**3 - x - 2'): ")
        a = float(input("Masukkan Nilai a: "))
        b = float(input("Masukkan Nilai b: "))
        root = regula_falsi(expresion_func, a, b, tol, maxiter)
        if root is not None:
            print(f"\nAkar (Metode Regula Falsi): {root:.6f}")
        else:
            print("\nMetode Regula Falsi tidak konvergen atau gagal.")

    if metode_pilihan == 3:
        g_func = input("Masukkan Fungsi Iterasi g(x) (contoh: '((x + 2/x) / 2)'): ")
        x0 = float(input("Masukkan nilai awal x0: "))
        root = fixed_point(g_func, x0, tol, maxiter)
        if root is not None:
            print(f"\nAkar (Iterasi Titik Tetap): {root:.6f}")
        else:
            print("\nMetode Iterasi Titik Tetap tidak konvergen atau gagal.")

    if metode_pilihan == 4:
        expresion_func = input("Masukkan Ekspresi f(x) (contoh: 'x**3 - x - 2'): ")
        expresion_func_turunan = input("Masukkan Turunan f'(x) (contoh: '3*x**2 - 1'): ")
        x0 = float(input("Masukkan nilai awal x0: "))
        root = newton_raphson(expresion_func, expresion_func_turunan, x0, tol, maxiter)
        if root is not None:
            print(f"\nAkar (Metode Newton-Raphson): {root:.6f}")
        else:
            print("\nMetode Newton-Raphson tidak konvergen atau gagal.")

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