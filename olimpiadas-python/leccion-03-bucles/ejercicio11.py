# Ejercicio 11: Muchas líneas
# Lee varias líneas, cada una con un número, e imprime PAR o IMPAR para cada una.
# Ejemplo: entrada 4, 7, 10 (una por línea) → salida PAR, IMPAR, PAR

import sys
for linea in sys.stdin:
    n = int(linea.strip())
    m = n %  2
         
    if  m == 0: 
        print("PAR")
    else:
        print("IMPAR")
