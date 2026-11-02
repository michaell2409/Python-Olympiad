# Ejercicio 13: La conjetura de Guacimara (Olimpiada de Tenerife 2026, ejercicio 1)
# Para cada número de la entrada, imprime los pasos hasta llegar a 1
# y la secuencia completa (sin el número inicial).
# Ejemplo: entrada 6 → salida 8 3 10 5 16 8 4 2 1 | entrada 1 → salida 0
# Primer problema de olimpiada real resuelto al 100 %.

import sys
for linea in sys.stdin:
    n=int(linea.strip())
    contador = 0 
    texto = ""
    while n != 1:
        contador = contador + 1   
        if n % 2 == 0: 
            n = n // 2
        else:
            n = n * 3 + 1 
        texto = texto + " " + str(n)
    print(str(contador) + texto)
