# Ejercicio 85: Todas las diagonales (práctica de matrices, ayuda para el ejercicio 83)
# Rellena una matriz n×n con 1..n² diagonal por diagonal, todas de arriba a abajo.
# Aprendido: hay 2n - 1 diagonales (de la 0 a la 2n - 2).
# Ejemplo: 3 → 1 2 4 / 3 5 7 / 6 8 9
# Tiempo: 39 minutos

n = int( input())
matriz=[["." for i in range(n)]for q in range(n)]

contador0 = 0
s = 0
resultado = 1 

while contador0 != n*2 - 1:
	for fila in range(n):
		columna = s - fila
		if 0 <= columna <= n -1:
			matriz[fila][columna] = resultado
			resultado = resultado + 1
	contador0 = contador0 + 1 
	s = s + 1 
			     



for linea in matriz:
	print(*linea)
