# Ejercicio 109: La conjetura de Guacimara (IV Olimpiada Informática de Tenerife 2026, P1)
# Por cada número N muestra los pasos de Collatz hasta llegar a 1 y la secuencia generada
# (par: /2, impar: *3+1). Si N es 1, muestra 0.
# Ejemplo: 6 → 8 3 10 5 16 8 4 2 1 | 1 → 0
# Tiempo: 12 minutos

import sys
for linea in sys.stdin:
	n = int(linea)
	lista = []
	contador = 0 
	if n == 1:
		print(0)
	else:
		while n != 1:
			if n % 2 == 0:
				lista.append(n//2)
				n = n // 2
			else:
				lista.append(n*3+1)
				n = n*3+1	     
		for i in lista:
			contador = contador +  1
		print(contador, *lista)
