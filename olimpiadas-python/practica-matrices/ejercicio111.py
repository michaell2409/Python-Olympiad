# Ejercicio 111: El cuadrado mágico
# Lee n (1-10) y una matriz n×n de números 0-99 y dice si es un cuadrado mágico:
# todas las filas, columnas y las dos diagonales suman lo mismo. Si la entrada está mal, ERROR.
# Ejemplo: 3 / 2 7 6 / 9 5 1 / 4 3 8 → MAGICO | 3 / 1 2 3 / 4 5 6 / 7 8 9 → NO MAGICO
# Tiempo: unas 2 horas (repartido en tres días; lo empecé de cero paso a paso y saqué las columnas yo solo)

import sys
linea = sys.stdin.read().split("\n")
if linea[0].isdigit() and linea[0].isascii() and 1 <= int(linea[0]) <= 10:
	n = int(linea[0])
	if len(linea) >= n + 1:
		matriz = []
		for i in range(1, n + 1):
			trozos = linea[i].split()
			fila = []
			if len(trozos) == n:
				for e in trozos:
					if e.isdigit() and e.isascii() and 0 <= int(e) <= 99:
						fila.append(int(e))
				
					else:
						print("ERROR")
						sys.exit()
				matriz.append(fila)		
			else:
				print("ERROR")
				sys.exit()

		interputor = True			
		objetivo = sum(matriz[0])	
		for fila in matriz:
			if sum(fila) != objetivo:
				interputor = False 
				
		

		ostias = []
		for i in range(n):
			u = 0
			for e in range(n):
				u = u + matriz[e][i]
			ostias.append(u)
		un = ostias[0]
		for i in ostias:
			if objetivo != i:
				interputor = False

		
		m = 0
		for i in range(n):
			m = m + matriz[i][i]

		q = 0	
		for i in range(n):
			q = q + matriz[n-i-1][i]
		if m != objetivo or q != objetivo:
			interputor = False 		
		if interputor == True:
			print("MAGICO")
		else:
			print("NO MAGICO")			

			









	else:
		print("ERROR")
		sys.exit()		


else:
	print("ERROR")
