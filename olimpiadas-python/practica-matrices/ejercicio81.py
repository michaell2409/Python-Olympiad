# Ejercicio 81: Un solo anillo (práctica de matrices)
# Ejercicio de ayuda que hice para poder resolver el ejercicio 80 (Los anillos):
# dibuja solo el anillo número a de una matriz n×n (a = 0 es el borde de fuera).
# Aprendido: el anillo a empieza en la fila/columna a y acaba en n-1-a.
# Ejemplo: 5 1 abcdefgh → . . . . . / . a b c . / . h . d . / . g f e . / . . . . .
# Tiempo: 57 minutos

n, a, palabra = input().split() 
n = int(n)
a = int(a)  

contador = 0
matriz  = [["."for i in range(n)] for q in range(n)]

for w in range(a, n-a):
	matriz[a][w] = palabra[contador % len(palabra)]
	contador = contador + 1 
	

for r in range(a+1, n-a-1):
	matriz[r][n-a-1] = palabra[contador%len(palabra)]
	contador = contador + 1
	

for e in range(n-a-1, a-1, -1):
	matriz[n-a-1][e] = palabra[contador % len(palabra)]
	contador = contador + 1 

for t in range(n-a-1-1, a, -1 ):
	matriz[t][a] = palabra[contador%len(palabra)]
	contador = contador + 1

for linea in matriz:
	print(*linea)
