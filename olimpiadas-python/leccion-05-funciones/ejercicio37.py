# Ejercicio 37: Capicúa (dando la vuelta a mano)
# Para cada línea, imprime SI si el número es capicúa o NO si no lo es.
# Ejemplo: 121 → SI | 123 → NO | 4554 → SI
# Idea: Construyo el número al revés letra a letra y lo comparo con el original.

import sys
def capicua(n):
	texto = ""
	n = str(n)
	u = len(n) 
	for i in range(u-1,-1,-1):
		texto = texto + n[i]
	return texto == n
for linea in sys.stdin:
	e = int(linea.strip())
	if capicua(e):
		print("SI")
	else:
		print("NO")
