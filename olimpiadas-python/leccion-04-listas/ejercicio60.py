# Ejercicio 60: Minas alrededor de una casilla (puente hacia el Buscaminas)
# Lee un tablero y una casilla F C; imprime cuántas minas hay en sus 8 vecinas.
# Ejemplo: tablero 4x4 *.*. / .... / .*.. / .... y casilla 1 1 → 3
# Idea: recorro el cuadrado de 3x3, salto las casillas fuera del tablero y resto la del centro si es mina.

m = int(input())
tablero = []
contador = 0

for i in range(m):
    tablero.append(input())

e, b  = map(int, input().split()) 

for q in range(e-1, e+2):
    for w in range(b-1, b+2):
        if  q >= 0 and w >= 0 and q < len(tablero) and w < len(tablero[0]) :
            if tablero[q][w] == "*":
                contador = contador + 1

if tablero[e][b] == "*":
            contador = contador -1 
print(contador)
