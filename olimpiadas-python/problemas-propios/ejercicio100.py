# Ejercicio 100: El camino de los primos (problema original creado para mi ejercicio 100)
# Rellena una matriz n×n en espiral con los números de las letras de una palabra (a=1 ... z=26)
# y cuenta con recursión cuántos caminos hay desde arriba a la izquierda hasta abajo a la derecha,
# moviéndose solo a la derecha o hacia abajo y pisando solo números primos.
# Mezcla todo lo aprendido: validación, letras→números, espiral, primos con e*e y recursión.
# Ejemplo: 4 Escoge → (matriz) y CAMINOS: 9 | 2 a → CAMINOS: 0 | 7 hola → ERROR
# Tiempo: unas 3 horas y media (repartido en dos días; tuve que repasar la espiral)

import string
entrada = input()
contador = 0

lista = []
if len(entrada) > 0 and not "  " in entrada and entrada[0] != " " and entrada[-1] != " ":
	entrada = entrada.split()
	if  len(entrada) == 2 and entrada[0].isdigit() and entrada[0].isascii() and 1 < int(entrada[0]) < 7  and  all(p.lower() in string.ascii_lowercase for p in entrada[1]): 
		contador = contador + 1
		n = int(entrada[0])
		matriz = [["" for i in range(n)]for q in range(n)]
		for i in entrada[1]:
			i = i.lower()
			casi = string.ascii_lowercase.index(i)	
			casi = casi + 1
			lista.append(casi)
		matriz = [["" for i in range(n)]for p in range(n)]
		a = 0
		contador1 = 0
		while a < (n +1) //2:
			if n % 2 != 0 and a == n//2:
				matriz[a][a] = lista[contador1 % len(lista)]
				a = a + 1 
			else:
				for i in range(a, n-a):
					matriz[a][i] = lista[contador1%len(lista)]
					contador1 = contador1 + 1 
				for q in range(a+1, n-a):
					matriz[q][n-1-a] = lista[contador1%len(lista)]
					contador1 = contador1 + 1 
				for w in range(n-a-2, a-1, -1):
					matriz[n-1-a][w] = lista[contador1%len(lista)]
					contador1 = contador1 + 1
				for r in range(n-a-2, a, -1 ):
					matriz[r][a] = lista[contador1%len(lista)]
					contador1 = contador1 + 1
				a = a + 1 	 			 	
		def esprimo(n):
			e = 2 
			if n < 2:
				return(False) 
			while e * e <= n:
				if n % e  == 0:
					return(False)
				e = e + 1  
			return(True)
		def caminos(f, c):
			
			if f >= n or c >= n:
				return 0
			
			if not esprimo(matriz[f][c]):
				return 0
			
			if f == n -1 and c == n-1:
				return 1
			
			return caminos(f+1, c) + caminos(f, c+1)

		for fila in matriz:
			print(*fila)
		print("CAMINOS:", caminos(0, 0)) 

if contador == 0:
	print("ERROR")
