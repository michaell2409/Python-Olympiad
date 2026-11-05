# Ejercicio 23: Collatz con listas
# Mismo problema que el 13 (olimpiada de Tenerife 2026), pero guardando
# la secuencia en una lista en vez de en un texto.
# Ejemplo: 6 → 8 3 10 5 16 8 4 2 1 | 1 → 0
# Idea: doy la vuelta a la lista para añadir el contador al principio.
# Lección 4: listas y textos

import sys
for linea in sys.stdin:
    n=int(linea.strip())
    contador = 0
    lista = []
    while n != 1:
        contador = contador+1 
        m = n % 2 
        if m == 0: 
            n=n // 2 
        else:    
            n=n * 3 + 1
        lista.append(n)
    lista1 = lista[::-1]
    lista1.append(contador)
    lista2 = lista1[::-1]
    print (*lista2)
