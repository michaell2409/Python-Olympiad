# Ejercicio 83: Matriz Diagonal Alterna (Olimpiada de Las Palmas 2026, ejercicio 4) - MI PRIMER P4
# Rellena una matriz n×n con 1..n² por diagonales (fila + columna = s), s = 0..2n-2;
# si s es par la diagonal va de abajo a arriba, si es impar de arriba a abajo. ERROR si n no es un entero de 1 a 30.
# Idea clave: recorrer todas las filas y calcular columna = s - fila (si cae fuera de la matriz, se salta).
# Lo partí en trozos: ejercicios 84 (una diagonal) y 85 (todas las diagonales).
# Ejemplo: 3 → 1 2 6 / 3 5 7 / 4 8 9
# Tiempo: 56 minutos (con los ejercicios 84 y 85 de por medio)

n = input().split()

if len(n) == 1 and n[0].isdigit() and n[0].isascii() and 1 <= int(n[0]) <= 30: 

	n = int(n[0])

	matriz=[["." for i in range(n)]for q in range(n)]

	contador0 = 0
	s = 0
	resultado = 1 

	while contador0 != n*2 - 1:
		if s % 2 == 0:
			for fila in range(n-1, -1, -1 ):
				columna = s - fila
				if 0 <= columna <= n -1:
					matriz[fila][columna] = resultado
					resultado = resultado + 1
		else:			
			for fila in range(n):
				columna = s - fila
				if 0 <= columna <= n -1:
					matriz[fila][columna] = resultado
					resultado = resultado + 1
		contador0 = contador0 + 1 
		s = s + 1 
					



	for linea in matriz:
		print(*linea)
else:
	print("ERROR")		
