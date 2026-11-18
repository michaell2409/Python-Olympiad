# Ejercicio 108: El Buscaminas de Fayna (IV Olimpiada Informática de Tenerife 2026, P6)
# Lee varios tableros M×N con minas (*) y casillas vacías (.) y muestra cada tablero con
# el número de minas que rodean a cada casilla vacía (8 vecinos), con una línea en blanco detrás.
# Ejemplo: 4 4 / *.*. / .... / .*.. / .... → *2*1 / 2321 / 1*10 / 1110
# Tiempo: 1 hora y 16 minutos (aprendí a leer varios casos seguidos con un puntero)

import sys 
linea = sys.stdin.read().split("\n")

pos = 0 
while  pos < len(linea) and linea[pos] != "":
	M, N = linea[pos].split()
	M = int(M)
	N = int(N)
	tablero = linea[pos +1 : pos +1 +M]  
	n1 = M
	n2 = N

	matriz = []
	matriz1 = [[0 for p in range(n2)]for i in range(n1)]

	matriz = tablero


	for i in range(n1):
		for p in range(n2):
			contador = 0 
			if matriz[i][p] == "*":
				matriz1[i][p] = "*"
			else:
				if i-1 >= 0:
					if matriz[i-1][p] == "*":
						contador = contador +  1 
				
				if i+1 < n1:
					if matriz[i+1][p] == "*":
						contador = contador +  1
				
				if p-1 >= 0:
					if matriz[i][p-1] == "*":
						contador = contador +  1 
				
				if p+1 < n2:
					if matriz[i][p+1] == "*":
						contador = contador +  1 
				
				if 0 <= i+1 < n1 and 0 <= p-1< n2:
					if matriz[i+1][p-1] == "*":
						contador = contador +  1
				
				if 0 <= i-1 < n1 and 0 <= p+1< n2:
					if matriz[i-1][p+1] == "*":
							contador = contador + 1 
							
				if 0 <= i+1 < n1 and 0 <= p+1< n2:
					if matriz[i+1][p+1] == "*":
						contador = contador +  1		
						
				if 0 <= i-1 < n1 and 0 <= p-1< n2:
					if matriz[i-1][p-1] == "*":
						contador = contador +  1		
				

				matriz1[i][p] = contador
	for fila in matriz1:
		print(*fila, sep="")
	print()
	pos = pos + M + 1
