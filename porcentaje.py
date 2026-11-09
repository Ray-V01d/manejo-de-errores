"""
Calcula el error relativo porcentual del valor teórico respecto al valor experimental

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def error_relativo_porcentual(teo, exp):
    """Devuelve |(teo - exp) / teo| * 100, con teo != 0."""
    if teo == 0:
        raise ValueError("v_teorico no puede ser 0")
    return math.fabs((teo - exp) / teo) * 100

def main():
    """Interfaz de línea de comandos: pide v_teorico y v_experimental e imprime el error %."""
    print("\033c", end="")
    print("PORCENTAJE = |(teo - exp) / teo| * 100")
    print("Digite los parámetros: v_teorico ; v_experimental")
    try:
        teo, exp = map(float, input().split())
    except (ValueError, EOFError):
        print("Digite dos números <float>")
        sys.exit(1)
    print()
    try:
        error = error_relativo_porcentual(teo, exp)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("Err% = ", round(error, 5), "%")

if __name__ == "__main__":
    main()
