"""
Exponencial: exp(x')

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def exponencial_con_error(x, dx):
    """Devuelve (exp(x), error) para x ± dx."""
    xy = math.exp(x)
    dxy = math.exp(x) * dx
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide x ± dx e imprime exp(x) ± error."""
    print("\033c", end="")
    print("EXPONENCIAL = exp(x')")
    print("digite los parámetros de: x ± dx ")
    try:
        x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 2 números <float>")
        sys.exit(1)
    print()
    xy, dxy = exponencial_con_error(x, dx)
    print(" exp(x') = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
