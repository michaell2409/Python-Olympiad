# Ejercicio 38: Capicúa (con [::-1])
# Mismo problema que el 37, resuelto de forma corta.
# Ejemplo: 121 → SI | 123 → NO | 4554 → SI
# Idea: [::-1] da la vuelta al texto de golpe.

import sys
def capicua(n):
	n = str(n)
	return n == n[::-1]
for linea in sys.stdin:
	i = int(linea.strip())
	if capicua(i):
		print("SI")
	else:
		print("NO")	
