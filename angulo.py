"""
Calcula el ángulo en la fórmula del plano inclinado

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def calcular_angulo(x):
    """Devuelve el ángulo en grados para el parámetro x (cm)."""
    if abs(x) > 69:
        raise ValueError("x debe estar en el rango [-69, 69]")
    return math.acos(1 - x**2 / 2380.5) * 180 / math.pi

def main():
    print("\033c", end="")
    print("ÁNGULO = acos(1 - x² / 2380.5)")
    print("Digite el parámetro x (cm):")
    try:
        x = float(input())
    except (ValueError, EOFError):
        print("Digite 1 número <float> en el rango [-69, 69]")
        sys.exit(1)
    print()
    theta = calcular_angulo(x)
    print("    Ángulo = ", round(theta, 5), " grados ")

if __name__ == "__main__":
    main()
