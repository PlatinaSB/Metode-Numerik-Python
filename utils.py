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