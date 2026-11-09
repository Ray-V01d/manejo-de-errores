"""
Multiplica un valor con error por una constante: a * x'

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def multiplicar_por_constante(a, x, dx):
    """Devuelve (resultado, error) de a * (x ± dx)."""
    return a * x, math.fabs(a * dx)

def main():
    """Interfaz de línea de comandos: pide a, x, dx e imprime el resultado."""
    print("\033c", end="")
    print("CONSTANTE = a * x'")
    print("Digite los parámetros: a ; x ± dx:")
    try:
        a, x, dx = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite 3 números <float>")
        sys.exit(1)
    print()
    xy, dxy = multiplicar_por_constante(a, x, dx)
    print("    a * x' = ", round(xy, 5), " ± ", round(dxy, 5))

if __name__ == "__main__":
    main()
