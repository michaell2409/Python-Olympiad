# Ejercicio 102: Girar la matriz
# Lee n (1-10) y n filas de n números (0-99) y muestra la matriz girada 90° a la derecha.
# Si falta algún número, hay letras o n no es válido, muestra ERROR.
# Ejemplo: 3 / 1 2 3 / 4 5 6 / 7 8 9 → 7 4 1 / 8 5 2 / 9 6 3
# Tiempo: unas 2 horas (repartido en dos días; me costó leer la matriz con sys.stdin)

import sys
linea = sys.stdin.read().split("\n")
xd = []
contador = 0
if len(linea) > 0 and linea[0].isdigit() and linea[0].isascii() and 1 <= int(linea[0]) <= 10:
	n = int(linea[0])
	matriz = [[""for i in range(n)]for q in range(n)]
	if len(linea) >= n+1: 
		for f in range(n):
			
			trozos = linea[f+1].split()
			if len(trozos) != n:
				print("ERROR")
				sys.exit()


			for c in range(n):
				if trozos[c].isdigit() and trozos[c].isascii() and 0 <= int(trozos[c]) <= 99:
					matriz[f][c] = int(trozos[c]) 
				else:
					print("ERROR")
					sys.exit()	
		
		
		for i in range(n):
			for p in range(n-1,-1, -1):
				xd.append(matriz[p][i])
		

		
		matriz1 = [["" for p in range(n) ]for t in range(n)]
		
		for i in range(n):
			for p in range(n):
				matriz1[i][p] = xd[contador % len(xd)]
				contador = contador + 1 
		
		for fila in matriz1:
			print(*fila)			
	
	else:
		print("ERROR")
		sys.exit()				


else:
	print("ERROR")	
