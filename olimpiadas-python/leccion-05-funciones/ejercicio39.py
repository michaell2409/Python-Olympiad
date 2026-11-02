# Ejercicio 39: ¿Está ordenada? (con sorted)
# Imprime ORDENADA si cada número es mayor o igual que el anterior, o DESORDENADA.
# Ejemplo: 1 3 3 7 9 → ORDENADA | 1 5 3 8 → DESORDENADA
# Idea: Si al ordenarla queda igual, es que ya estaba ordenada.

def orden(n):
	m = sorted(n)
	return m == n 
listirijilla = list(map(int, input().split()))
if orden(listirijilla):
	print("ORDENADA")
else:
	print("DESORDENADA")
