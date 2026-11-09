"""
Tangente: tan(x')

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def tangente_con_error(x, dx):
    """Devuelve (tan(x), error) para θ ± dθ en radianes."""
    if math.cos(x) == 0:
        raise ValueError("x está en una asíntota de tan(x) (cos(x) = 0)")
    xy = math.tan(x)
    dxy = dx / math.cos(x) ** 2
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide θ ± dθ e imprime tan(θ) ± error."""
    print("\033c", end="")
    print("TANGENTE = tan(x')")
    print("Digite los parámetros de θ (en radianes): θ ± dθ")
    try:
        x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite dos números <float>")
        sys.exit(1)
    print()
    try:
        xy, dxy = tangente_con_error(x, dx)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("    tan(x') = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
