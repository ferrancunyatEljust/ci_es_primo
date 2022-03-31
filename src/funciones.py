"""Módulo que contiene la función es_primo"""
import math


def es_primo(entero):
    """
    Función para determinar si un número es primo:

    Entrada:
    - entero: número entero a determinar si es primo

    Salida:
    - True/False: en caso de ser primo o no
    """
    if entero < 2:
        return False
    for factor in range(2, math.floor(math.sqrt(entero) + 1)):
        if entero % factor == 0:
            return False
    return True
