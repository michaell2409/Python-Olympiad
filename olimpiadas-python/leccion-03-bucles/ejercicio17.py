# Repaso 4: Múltiplos de 3
# Para cada línea con un número N, imprime cuántos números entre 1 y N son múltiplos de 3.
# Ejemplo: 10 → 3 | 3 → 1 | 2 → 0
# Nota: también se podría hacer sin bucle con n // 3.

import sys 
for linea in sys.stdin:
	n = int(linea.strip())
	contador = 0
	for i in range (1,(n+1)):
	    m = i % 3
	    if m == 0:  
	        contador = contador + 1
	print (contador)
