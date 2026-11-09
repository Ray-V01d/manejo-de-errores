"""
Coseno: cos(x')

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def coseno_con_error(x, dx):
    """Devuelve (cos(x), error) para θ ± dθ en radianes."""
    xy = math.cos(x)
    y_max = math.cos(x + dx)
    y_min = math.cos(x - dx)
    dxy = max(math.fabs(y_max - xy), math.fabs(y_min - xy))
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide θ ± dθ e imprime cos(θ) ± error."""
    print("\033c", end="")
    print("COSENO = cos(x')")
    print("Digite los parámetros de θ (en rad): θ ± dθ:")
    try:
        x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 2 números <float>")
        sys.exit(1)
    print()
    xy, dxy = coseno_con_error(x, dx)
    print("    cos(x') = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
