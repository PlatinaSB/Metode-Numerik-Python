from utils import eval_expresion

def bisection(expresion_func, a, b, tol=1e-6, maxiter=100):
    """
    Menerapkan metode bagi dua untuk menemukan akar dari sebuah fungsi.
    """
    fa = eval_expresion(expresion_func, a)
    fb = eval_expresion(expresion_func, b)

    if fa is None or fb is None:
        return None

    if fa * fb >= 0:
        print("Metode gagal: f(a) dan f(b) harus memiliki tanda yang berbeda.")
        return None

    print(f'{"i":>2} {"a":>10} {"b":>10} {"x":>10} {"f(a)":>15} {"f(b)":>15} {"f(x)":>15}')
    i = 0
    while abs(b - a) > tol:
        if i >= maxiter:
            print(f"Metode tidak konvergen dalam iterasi maksimum ({maxiter}).")
            return None
        
        x = (a + b) / 2.0
        fx = eval_expresion(expresion_func, x)

        if fx is None:
            return None

        print(f'{i+1:2d} {a:10.6f} {b:10.6f} {x:10.6f} {fa:15.8f} {fb:15.8f} {fx:15.8f}')

        if abs(fx) < tol:
            return x
        
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
        i += 1
    return (a + b) / 2.0