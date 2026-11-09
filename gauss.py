"""
Calcula el valor promedio, la desviación estandar y el error del valor medio de un conjunto de datos experimentales

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

import sys
import math

def estadisticas(datos):
    """Devuelve (media, desviación estándar, error del valor medio) de una lista de datos."""
    n = len(datos)
    if n < 2:
        raise ValueError("Se necesitan al menos 2 datos")
    prom = sum(datos) / n
    cua = sum((dato - prom) ** 2 for dato in datos)
    sigma = math.sqrt(cua / (n - 1))
    error = sigma / math.sqrt(n)
    return prom, sigma, error

def main():
    """Interfaz de línea de comandos: pide los datos e imprime media, σ y error."""
    print("\033c", end="")
    print("PROMEDIO = sum(d1, d2, d3, ..., dn) / n")
    print("Calcula el valor medio, la desviación estándar y el error en la medida")
    print("Introduzca los datos...")
    try:
        datos = list(map(float, input().split()))
    except (ValueError, EOFError):
        print("Ingrese valores válidos")
        sys.exit(1)
    print()
    try:
        prom, sigma, error = estadisticas(datos)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print("Conteo = ", len(datos))
    print("Media (mesurando) = ", round(prom, 5))
    print("Desviación estándar = ", round(sigma, 5))
    print("Error del valor = ", round(error, 5))

if __name__ == "__main__":
    main()
