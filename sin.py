"""
Seno: sin(x')

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def seno_con_error(x, dx):
    """Devuelve (sin(x), error) para θ ± dθ en radianes."""
    xy = math.sin(x)
    dxy = abs(math.cos(x)) * dx
    return xy, dxy

def main():
    """Interfaz de línea de comandos: pide θ ± dθ e imprime sin(θ) ± error."""
    print("\033c", end="")
    print("SENO = sin(x')")
    print("Digite los parámetros de θ (en radianes): θ ± dθ")
    try:
        x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite dos números <float>")
        sys.exit(1)
    print()
    xy, dxy = seno_con_error(x, dx)
    print("    sin(x') = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
