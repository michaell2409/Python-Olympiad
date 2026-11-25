# Ejercicio 114: La matriz simétrica
# Lee n (1-10) y una matriz n×n de números 0-99 y dice si es simétrica:
# cada casilla (f, c) tiene que valer lo mismo que la casilla (c, f). Si la entrada está mal, ERROR.
# Ejemplo: 3 / 1 2 3 / 2 5 4 / 3 4 9 → SIMETRICA | 3 / 1 2 3 / 7 5 4 / 3 4 9 → NO SIMETRICA
# Tiempo: 50 minutos (la idea de la simetría la pensé yo antes de programar)

import sys
linea = sys.stdin.read().split("\n")

if  linea[0].isdigit() and linea[0].isascii() and 1 <= int(linea[0]) <= 10 and len(linea) >= int(linea[0])+1:
	n = int(linea[0])
	matriz = [] 
	for i in range(1,n+1):
		fila = []
			
			
		trozos = linea[i].split()
		if len(trozos) != n:
			print("ERROR")
			sys.exit() 
		for e in trozos:
			
			
			if not (e.isdigit() and e.isascii()):
				print("ERROR")
				sys.exit()

			e = int(e)
			if 0 <= e <= 99:
				fila.append(e)	

			

			else:
				print("ERROR")
				sys.exit()
		matriz.append(fila)		
	
	simetrica = True
	for e in range(n):
		for f in range(n):
			if matriz[e][f] != matriz[f][e]:
				simetrica = False
	if simetrica == True:
		print("SIMETRICA")
	else:
		print("NO SIMETRICA")				 				 	   

else:
	print("ERROR")
