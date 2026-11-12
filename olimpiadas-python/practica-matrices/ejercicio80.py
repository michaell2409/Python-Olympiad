# Ejercicio 80: Los anillos (práctica de matrices, preparación para la Matriz Espiral)
# Rellena todos los anillos de una matriz n×n de fuera a dentro; cada anillo da una vuelta → ↓ ← ↑
# y vuelve a empezar la palabra. Aquí me atasqué y tuve que hacer el ejercicio 81 para desatascarme.
# Idea mía: si llego a la mitad ya he recorrido toda la matriz ((n+1)//2 anillos),
# y el centro de una casilla (n impar) lo arreglo al final.
# Ejemplo: 5 abcdefgh → a b c d e / h a b c f / g h a d g / f g f e h / e d c b a
# Tiempo: 1 hora y 23 minutos

n,  palabra = input().split() 
n = int(n)
 
a = 0  


matriz  = [["."for i in range(n)] for q in range(n)]
while a < (n+1)//2:
	contador = 0
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

	a = a + 1 
	
if n % 2 != 0:
	q = n//2
	matriz[q][q] = palabra[0] 
for linea in matriz:
	print(*linea)
