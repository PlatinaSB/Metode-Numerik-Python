from utils import eval_expresion

def newton_raphson(expresion_func, expresion_func_turunan, x0, tol=1e-6, maxiter=100):
    """
    Menerapkan metode Newton-Raphson untuk menemukan akar dari sebuah fungsi.
    """
    print(f'{"i":>2} {"x_i":>15} {"f(x_i)":>15} {"f\'(x_i)":>15} {"|x_i+1 - x_i|":>20}')
    i = 0
    while True:
        if i >= maxiter:
            print(f"Metode tidak konvergen dalam iterasi maksimum ({maxiter}).")
            return None
        
        fx = eval_expresion(expresion_func, x0)
        dfx = eval_expresion(expresion_func_turunan, x0)

        if fx is None or dfx is None:
            return None

        if dfx == 0:
            print("Turunan nol. Metode gagal.")
            return None
        
        x1 = x0 - fx / dfx
        selisih = abs(x1 - x0)
        print(f'{i+1:2d} {x0:15.8f} {fx:15.8f} {dfx:15.8f} {selisih:20.8f}')
        
        if selisih < tol:
            return x1
        x0 = x1
        i += 1