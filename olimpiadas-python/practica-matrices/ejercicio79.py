# Ejercicio 79: El marco (práctica de matrices, preparación para la Matriz Espiral)
# Rellena solo el borde de una matriz n×n dando una vuelta en el sentido de las agujas del reloj, sin repetir esquinas.
# Ejemplo: 4 abcdefghijkl → a b c d / l . . e / k . . f / j i h g
# Tiempo: 28 minutos

n, palabra = input().split() 
n = int(n)  

contador = 0
matriz  = [["."for i in range(n)] for q in range(n)]

for w in range(n):
	matriz[0][w] = palabra[contador % len(palabra)]
	contador = contador + 1 

for r in range(1,n-1):
	matriz[r][n-1] = palabra[contador%len(palabra)]
	contador = contador + 1 

for e in range(n-1, -1, -1):
	matriz[n-1][e] = palabra[contador % len(palabra)]
	contador = contador + 1 

for t in range(n-2, 0, -1):
	matriz[t][0] = palabra[contador%len(palabra)]
	contador = contador + 1

for linea in matriz:
	print(*linea)
