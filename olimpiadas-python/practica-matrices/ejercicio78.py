# Ejercicio 78: Ida y vuelta (práctica de matrices, preparación para la Matriz Espiral)
# Rellena la primera fila de izquierda a derecha y la última de derecha a izquierda, siguiendo la palabra y repitiéndola si se acaba.
# Aprendido: entrada en una línea con split(), range hacia atrás (range(n-1, -1, -1)) y el % para que la palabra dé la vuelta.
# Ejemplo: 4 abcdef → a b c d / . . . . / . . . . / b a f e
# Tiempo: 39 minutos

n, palabra = input().split() 
n = int(n)  

contador = 0
while contador == len(palabra):
	contador = 0
matriz  = [["."for i in range(n)] for q in range(n)]
for w in range(n):
	matriz[0][w] = palabra[contador]
	contador = contador + 1
	while contador == len(palabra):
		contador = 0
for e in range(n-1, -1, -1):
	matriz[n-1][e] = palabra[contador % len(palabra)]
	contador = contador + 1 
for linea in matriz:
	print(*linea)
