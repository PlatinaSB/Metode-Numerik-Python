import numpy as np

safe_dict = {
    "np": np,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "exp": np.exp,
    "log": np.log,
    "sqrt": np.sqrt,
    "abs": np.abs,
    "pi": np.pi,
    "e": np.e,
    "pow": np.power,
    "arcsin": np.arcsin,
    "arccos": np.arccos,
    "arctan": np.arctan,
}

def eval_expresion(ekspresi, nilai_x):
    """
    Mengevaluasi ekspresi string matematika dengan nilai x tertentu.
    Menggunakan kamus aman untuk mencegah eksekusi kode berbahaya.
    """
    try:
        return eval(ekspresi, {"__builtins__": None}, safe_dict | {"x": nilai_x})
    except Exception as e:
        print(f"Error saat mengevaluasi ekspresi '{ekspresi}': {e}")
        return None

def get_float_optional(prompt, default):
    """
    Meminta input float dari pengguna, dengan opsi default jika input kosong.
    Termasuk validasi input.
    """
    while True:
        val = input(prompt)
        if not val.strip():
            return default
        try:
            return float(val)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka atau kosongkan untuk nilai default.")

def get_int_optional(prompt, default):
    """
    Meminta input integer dari pengguna, dengan opsi default jika input kosong.
    Termasuk validasi input.
    """
    while True:
        val = input(prompt)
        if not val.strip():
            return default
        try:
            return int(val)
        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat atau kosongkan untuk nilai default.")