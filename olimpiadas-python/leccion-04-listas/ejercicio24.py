# Ejercicio 24: Contar pares
# Lee una línea con varios números e imprime cuántos son pares.
# Ejemplo: 3 8 5 2 10 → 3
# Idea: guardo los pares en otra lista y cuento cuántos hay con len.

numeros = list(map(int, input().split()))
otro = []
for n in numeros:
	m = n % 2
	if  m == 0: 
		otro.append(n)
resultado = len(otro)
print(resultado)
