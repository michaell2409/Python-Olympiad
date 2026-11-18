# Ejercicio 103: Los vecinos
# Lee n (1-10) y una matriz n×n de números 0-99 y muestra otra matriz donde cada casilla
# vale la suma de sus vecinos de arriba, abajo, izquierda y derecha (si existen).
# Ejemplo: 3 / 1 2 3 / 4 5 6 / 7 8 9 → 6 9 8 / 13 20 17 / 12 21 14 | entrada mal formada → ERROR
# Tiempo: 55 minutos

import sys
linea = sys.stdin.read().split("\n")
lista = []
contador = 0   
I = 0
P = 0
if linea[0].isdigit() and linea[0].isascii() and len(linea) >= int(linea[0]) + 1 and 1 <= int(linea[0]) <= 10:
	n = int(linea[0])
	for i in range(1,n+1):
		trozos = linea[i].split()
		
		if n != len(trozos):
			print("ERROR")
			sys.exit()
		for p in trozos:
			if not(p.isdigit() and p.isascii() and 0 <= int(p) <= 99):
				print("ERROR")
				sys.exit()
			lista.append(int(p))
	matriz = [["" for i in range(n)]for p in range(n)]
	for i in range(n):
		for p in range(n):
			matriz[i][p] = lista[contador]
			contador = contador + 1
	matriz1 = [[0 for i in range(n) ]for p in range(n)]

	for i in range(n):
		for p in range(n):
			if i+1 < n:
				matriz1[i][p] = matriz1[i][p] + matriz[i+1][p]
			if i-1 >= 0:
				matriz1[i][p] = matriz1[i][p] + matriz[i-1][p]
			if p+1 < n:
				matriz1[i][p] = matriz1[i][p] + matriz[i][p+1]
			if p-1 >= 0:
				matriz1[i][p] = matriz1[i][p] + matriz[i][p-1]

	for fila in matriz1:
		print(*fila)						
			  			





else:
	print("ERROR")
