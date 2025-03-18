#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def procesar_rango(inicio, fin):
    """Calcula y muestra los factoriales en el rango especificado."""
    for i in range(inicio, fin + 1):
        print(f"Factorial {i}! es {factorial(i)}")



if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ejemplo: 5, 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]



if "-" in entrada:
    partes = entrada.split("-")
    if entrada.startswith("-"):  # Caso "-10"  de 1 a 10
        inicio, fin = 1, int(partes[1])
    elif entrada.endswith("-"):  # Caso "5-"  de 5 a 60
        inicio, fin = int(partes[0]), 60
    else:  # Caso "4-8"  de 4 a 8
        inicio, fin = int(partes[0]), int(partes[1])
    procesar_rango(inicio, fin)
else:
    num = int(entrada)
    print(f"Factorial {num}! es {factorial(num)}")