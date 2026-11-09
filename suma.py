"""
Suma dos valores con error

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def suma_con_error(x, dx, y, dy):
    """Devuelve (x + y, error) para (x ± dx) + (y ± dy)."""
    xy = x + y
    dxy = math.sqrt(dx**2 + dy**2)
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide x ± dx ; y ± dy e imprime la suma."""
    print("\033c", end="")
    print("SUMA = x' + y'")
    print("Digite los parámetros: x ± dx ; y ± dy")
    try:
        x, dx, y, dy = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 4 números <float>")
        sys.exit(1)
    print()
    xy, dxy = suma_con_error(x, dx, y, dy)
    print("    x' + y' = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
