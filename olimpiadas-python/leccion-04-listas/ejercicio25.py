# Ejercicio 25: Solo los grandes
# Lee una lista e imprime solo los números mayores que 10, en el mismo orden.
# Ejemplo: 5 12 3 40 11 → 12 40 11

numeros = list(map(int, input().split()))
otro = []
u = len(numeros)
for i in range(0,u):
	if numeros[i] > 10:
		otro.append(numeros[i])
print(*otro)
