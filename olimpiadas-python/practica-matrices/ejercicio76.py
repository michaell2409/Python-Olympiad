# Ejercicio 76: Esquinas de una matriz (práctica de matrices)
# Crea una matriz 3x3 como lista de listas, pone una x en las 4 esquinas y una o en el centro, y la imprime.
# Aprendido: crear la matriz con [[...] for ...] (no con * n), acceder con matriz[fila][columna] e imprimir con print(*fila).
# Tiempo: 15 minutos

matriz = [[" " for i in range(3)]for n in range(3)]
matriz[0][2] = "x"
matriz[2][0] = "x"
matriz[0][0] = "x"
matriz[2][2] = "x"
matriz[1][1] = "o"
for line in matriz:
	print(*line)
