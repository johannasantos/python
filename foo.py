import numbers

def cuad(n):
    """Devuelve el cuad del nro."""
    if not isinstance(n, numbers.Number):
        raise TypeError("Solo nros")
    return n ** 2

def store(n, fpath):
    """Guarda el nro en disco."""
    if n == 0:
        return
    with open(fpath, "wt", encoding="ascii") as fh:
        fh.write(str(n))
