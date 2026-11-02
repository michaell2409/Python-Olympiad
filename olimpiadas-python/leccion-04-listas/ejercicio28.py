# Ejercicio 28: Sumar dos listas
# Lee dos listas del mismo tamaño e imprime la suma de cada pareja en la misma posición.
# Ejemplo: 1 2 3 y 10 20 30 → 11 22 33

lista1 = list(map(int, input().split())) 
lista2 = list(map(int, input().split()))
resultado = [] 
u = len(lista1)
for i in range(0,u):
	m = lista1[i] + lista2[i]
	resultado.append(m)
print(*resultado)
