# Ejercicio 34: Números amigos (Olimpiada de Tenerife 2026, ejercicio 2)
# A y B son amigos si la suma de divisores propios de A es B y la de B es A.
# Ejemplo: 220 284 → AMIGOS | 100 200 → NO AMIGOS | 1 1 → AMIGOS (caso especial)
# Idea: Llamo dos veces a la misma función, una con A y otra con B.

import sys
def sumadedivisores(a):
	suma = 0
	for i in range(1,a):
		if a % i == 0:
			suma = suma + i
	return  suma		 
for linea in sys.stdin:
	n = list(map(int, linea.split()))
	if n[1] == 1 and n[0] == 1:
		print("AMIGOS") 
	elif sumadedivisores(n[0]) == n[1] and sumadedivisores(n[1]) == n[0]:
		print("AMIGOS")
	else:
		print("NO AMIGOS")	
