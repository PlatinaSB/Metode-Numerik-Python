from utils import eval_expresion

def fixed_point(g_func, x0, tol=1e-6, maxiter=100):
    """
    Menerapkan metode iterasi titik tetap untuk menemukan akar dari sebuah fungsi.
    """
    print(f'{"i":>2} {"x_i":>15} {"x_i+1":>15} {"|x_i+1 - x_i|":>20}')
    i = 0
    while True:
        if i >= maxiter:
            print(f"Metode tidak konvergen dalam iterasi maksimum ({maxiter}).")
            return None
        
        x1 = eval_expresion(g_func, x0)
        if x1 is None:
            return None

        selisih = abs(x1 - x0)
        print(f'{i+1:2d} {x0:15.8f} {x1:15.8f} {selisih:20.8f}')
        
        if selisih < tol:
            return x1
        x0 = x1
        i += 1