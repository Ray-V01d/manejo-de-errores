"""
Logaritmo natural ln(x')

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def logaritmo_con_error(x, dx):
    """Devuelve (ln(x), error) para x ± dx, con x > 0."""
    if x <= 0:
        raise ValueError("x debe ser mayor que 0 para ln(x)")
    logx = math.log(x)
    dlogx = dx / x
    return logx, dlogx

def main():
    """Interfaz de línea de comandos: pide x ± dx e imprime ln(x) ± error."""
    print("\033c", end="")
    print("LOGARITMO = ln(x')")
    print("Digite el parámetro: x ± dx")
    try:
        x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Ingrese 2 números <float>")
        sys.exit(1)
    print()
    try:
        logx, dlogx = logaritmo_con_error(x, dx)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("ln(x') = ", round(logx, 5), " ± ", round(dlogx, 5))

if __name__ == "__main__":
    main()
