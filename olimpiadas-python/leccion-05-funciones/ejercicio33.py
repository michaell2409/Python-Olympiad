# Ejercicio 33: Suma de cifras
# Para cada línea, imprime la suma de las cifras del número.
# Ejemplo: 2026 → 10 | 999 → 27
# Idea: Convierto el número en texto y recorro sus cifras una a una.

import sys
def suma_cifras(n):
	contador = 0	
	for i in str(n):
		contador = contador + int(i)
	return contador		 
for linea in sys.stdin:
	l = int(linea.strip())
	print(suma_cifras(l)) 
