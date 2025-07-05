from utils import eval_expresion

def secant(expresion_func, x0, x1, tol=1e-6, maxiter=100):
    """
    Menerapkan metode Secant untuk menemukan akar dari sebuah fungsi.
    """
    print(f'{"i":>2} {"x_i-1":>15} {"x_i":>15} {"x_i+1":>15} {"f(x_i)":>15} {"|x_i+1 - x_i|":>20}')
    i = 0
    while True:
        if i >= maxiter:
            print(f"Metode tidak konvergen dalam iterasi maksimum ({maxiter}).")
            return None
        
        fx0 = eval_expresion(expresion_func, x0)
        fx1 = eval_expresion(expresion_func, x1)

        if fx0 is None or fx1 is None:
            return None

        if fx1 - fx0 == 0:
            print("Pembagian nol (f(x1) - f(x0) = 0). Metode gagal.")
            return None
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        selisih = abs(x2 - x1)
        print(f'{i+1:2d} {x0:15.8f} {x1:15.8f} {x2:15.8f} {fx1:15.8f} {selisih:20.8f}')
        
        if selisih < tol:
            return x2
        x0, x1 = x1, x2
        i += 1