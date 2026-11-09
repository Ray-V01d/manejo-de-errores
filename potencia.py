"""
Calcula una cantidad con error elevada a una constante

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def potencia_con_error(x, dx, n):
    """Devuelve (x**n, error) para (x ± dx)**n."""
    if x == 0 and n < 1:
        raise ValueError("x no puede ser 0 con n < 1 (derivada indefinida)")
    xy = math.pow(x, n)
    dxy = abs(n * math.pow(x, n - 1)) * dx
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide x ± dx ; n e imprime (x')ⁿ ± error."""
    print("\033c", end="")
    print("POTENCIA = (x')ⁿ")
    print("Digite los parámetros: x ± dx ; n")
    try:
        x, dx, n = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 3 números <float>")
        sys.exit(1)
    print()
    try:
        xy, dxy = potencia_con_error(x, dx, n)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("    (x')ⁿ = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
