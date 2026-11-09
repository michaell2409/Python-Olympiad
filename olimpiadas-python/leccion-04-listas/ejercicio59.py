# Ejercicio 59: Contar las minas de un tablero (puente hacia el Buscaminas)
# Lee M y luego M filas de un tablero con minas (*) y casillas vacías (.); imprime cuántas minas hay.
# Ejemplo: 3 / *.*. / .... / .*.. → 3
# Idea: un tablero es una lista de textos; tablero[fila][columna] es una casilla.

m = int(input())
tablero = []
contador = 0

for i in range(m):
    tablero.append(input())

for q in range(len(tablero)):
    for w in range(len(tablero[q])):
       if tablero[q][w] == "*":
        contador = contador + 1 

print(contador)
