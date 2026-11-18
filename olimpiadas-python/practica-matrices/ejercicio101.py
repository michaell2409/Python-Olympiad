# Ejercicio 101: La serpiente
# Lee n (1-10) y rellena una matriz n×n con los números del 1 al n*n en zigzag:
# las filas pares de izquierda a derecha y las impares de derecha a izquierda.
# Ejemplo: 3 → 1 2 3 / 6 5 4 / 7 8 9 | 0 → ERROR
# Tiempo: 49 minutos

entrada = input()
contador1 = 0
contador = 1 
if len(entrada) > 0 and  "  "  not in entrada and entrada[0] != " ":  
	entrada = entrada.split()
	if len(entrada) == 1 and entrada[0].isdigit() and entrada[0].isascii() and 0 < int(entrada[0]) < 11:
		contador1 = contador1 + 1  
		numero = int(entrada[0])
		matriz = [["" for i in range(numero)]for p in range(numero)]
		

		for fila in range(numero):
			if fila % 2 == 0:
				for i in range(0,numero):
					matriz[fila][i] = contador
					contador = contador + 1 
			else:
				for p in range(numero-1,0-1, - 1):
					matriz[fila][p] = contador
					contador = contador + 1	




		for i in matriz:
			print(*i)
if contador1 == 0:
	print("ERROR") 
