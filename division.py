"""
Divide dos cantidades con error

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def dividir_con_error(x, dx, y, dy):
    """Devuelve (x/y, error) para (x ± dx) / (y ± dy)."""
    if y == 0:
        raise ValueError("El divisor y no puede ser 0")
    xy = x / y
    dxy = abs(x / y) * math.sqrt((dx / x) ** 2 + (dy / y) ** 2)
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide x ± dx ; y ± dy e imprime el cociente."""
    print("\033c", end="")
    print("DIVISIÓN = x' / y'")
    print("Digite los parámetros: x ± dx ; y ± dy:")
    try:
        x, dx, y, dy = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 4 números <float>")
        sys.exit(1)
    print()
    try:
        xy, dxy = dividir_con_error(x, dx, y, dy)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print(" x'/y' = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
