# Ejercicio 62: El Buscaminas con un solo tablero (puente hacia el Buscaminas)
# Lee M N y un tablero; cambia cada casilla vacía por el número de minas que tiene alrededor.
# Ejemplo: 2 3 / ..* / ... → 01* / 011
# Idea: construyo cada fila letra a letra y, cuando mide N, la guardo en la lista de resultados.

m = list(map(int, input().split()))
tablero = []

resultado = []

for i in range(m[0]):
    tablero.append(input())
palabra = ""
 

    

for r in range(0, len(tablero)):
    for t in range(0, m[1]):
        contador = 0
        if tablero[r][t] == "*":
            palabra = palabra + "*"
            while len(palabra) == m[1]:
                resultado.append(palabra)
                palabra = ""
        else:    
            for q in range(r-1, r+2):
                for w in range(t-1, t+2):
                    if q >= 0 and w >= 0 and q <= m[0]-1 and w <= m[1]-1:  
                        if tablero[q][w] == "*":
                            contador = contador + 1 
            palabra = palabra + str(contador)
            while len(palabra) == m[1]:
                resultado.append(palabra)
                palabra = ""             

for u in resultado:
    print(u)
