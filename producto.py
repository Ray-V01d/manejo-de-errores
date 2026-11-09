"""
Multiplica dos valores con error

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def producto_con_error(x, dx, y, dy):
    """Devuelve (x*y, error) para (x ± dx) * (y ± dy)."""
    if x == 0 or y == 0:
        raise ValueError("x e y deben ser distintos de 0 (errores relativos)")
    xy = x * y
    dxy = abs(xy) * math.sqrt((dx / x) ** 2 + (dy / y) ** 2)
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide x ± dx ; y ± dy e imprime el producto."""
    print("\033c", end="")
    print("PRODUCTO = x' * y'")
    print("Digite los parámetros: x ± dx ; y ± dy")
    try:
        x, dx, y, dy = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 4 números <float>")
        sys.exit(1)
    print()
    try:
        xy, dxy = producto_con_error(x, dx, y, dy)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("    x'*y' = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
