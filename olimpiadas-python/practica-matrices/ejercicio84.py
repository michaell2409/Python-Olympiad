# Ejercicio 84: Una diagonal (práctica de matrices, ayuda para el ejercicio 83)
# Dibuja con # la diagonal s de una matriz n×n: las casillas donde fila + columna = s.
# Aprendido: columna = s - fila, y comprobar que 0 <= columna <= n - 1.
# Ejemplo: 4 2 → . . # . / . # . . / # . . . / . . . .
# Tiempo: 1 hora y 13 minutos

n, s = map(int, input().split())
matriz=[["." for i in range(n)]for q in range(n)]

for fila in range(n):
	columna = s - fila
	if 0 <= columna <= n -1:
		matriz[fila][columna] = "#"   



for linea in matriz:
	print(*linea)
