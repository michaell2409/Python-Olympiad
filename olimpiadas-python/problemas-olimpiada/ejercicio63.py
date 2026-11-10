# Ejercicio 63: El Buscaminas de Fayna (Olimpiada de Tenerife 2026, ejercicio 6)
# Varios tableros seguidos; cada uno empieza con M N y luego M filas con minas (*) y vacías (.).
# Para cada tablero, cambia cada casilla vacía por el número de minas de sus 8 vecinas.
# Ejemplo: 2 3 / ..* / ... → 01* / 011

import sys 
for linea in sys.stdin:
	n = list(map(int , linea.split()))
	tablero = []

	resultado = []

	for i in range(n[0]):
	    tablero.append(input())
	palabra = ""
 

    

	for r in range(0, len(tablero)):
	    for t in range(0, n[1]):
	        contador = 0
	        if tablero[r][t] == "*":
	            palabra = palabra + "*"
	            while len(palabra) == n[1]:
	                resultado.append(palabra)
	                palabra = ""
	        else:    
	            for q in range(r-1, r+2):
	                for w in range(t-1, t+2):
	                    if q >= 0 and w >= 0 and q <= n[0]-1 and w <= n[1]-1:  
	                        if tablero[q][w] == "*":
	                            contador = contador + 1 
	            palabra = palabra + str(contador)
	            while len(palabra) == n[1]:
	                resultado.append(palabra)
	                palabra = ""             

	for u in resultado:
		print(u)
