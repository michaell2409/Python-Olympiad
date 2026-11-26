# Ejercicio 115: Fila y columna ganadoras
# Lee n (1-10) y una matriz n×n de números 0-99 y muestra la fila y la columna que más suman
# (numeradas desde 1; en empate gana la de número más pequeño). Si la entrada está mal, ERROR.
# Ejemplo: 3 / 1 2 3 / 4 5 6 / 7 8 9 → FILA 3 24 / COLUMNA 3 18
# Tiempo: 49 minutos (escribí la lectura y la validación de memoria, sin copiar)

import sys
linea = sys.stdin.read().split("\n")
if  linea[0].isdigit() and linea[0].isascii() and 1 <= int(linea[0]) <= 10 and len(linea) > int(linea[0]):
	n = int(linea[0])
	matriz = []
	for i in range(1,n+1):
		otrico = []
		otro = linea[i].split()
		if len(otro) != n:
			print("ERROR")
			sys.exit() 
		for e in otro:
			
			if not (e.isdigit() and e.isascii() and 0 <= int(e) <= 99):
				print("ERROR")
				sys.exit()
			else:
				e = int(e)
				otrico.append(e)	
		matriz.append(otrico)	
	filas = []
	columnas = []
	for fila in matriz:
		q = sum(fila)
		filas.append(q)

	for i in range(n):
		w = 0
		for e in range(n):
			w = matriz[e][i] + w 
		columnas.append(w)	


	print(f"FILA {filas.index(max(filas))+1} {max(filas)}")
	
	print(f"COLUMNA {columnas.index(max(columnas))+1} {max(columnas)}")			


else:
	print("ERROR")
