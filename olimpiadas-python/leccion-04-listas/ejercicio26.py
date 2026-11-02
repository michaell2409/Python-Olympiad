# Ejercicio 26: ¿En qué posición está?
# Lee una lista y un número; imprime la posición de la primera vez que aparece, o -1.
# Ejemplo: 4 7 1 7 9 y 7 → 1
# Idea: Guardo todas las posiciones y me quedo con la primera.

lista = list(map(int, input().split() ))
buscar = int(input())
u = len(lista)
lista1 = []
lista2 = [] 
for i in range(0,u):
	if buscar == lista[i]:
		lista1.append(i)
if lista1 == lista2:
	print(-1)
else:
	print(lista1[0])
