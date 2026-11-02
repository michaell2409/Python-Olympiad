# Ejercicio 40: ¿Está ordenada? (recorriendo parejas)
# Mismo problema que el 39, sin sorted.
# Ejemplo: 1 3 3 7 9 → ORDENADA | 1 5 3 8 → DESORDENADA
# Idea: return False en cuanto encuentro una pareja mal; return True si termino el bucle.

def otra(n):
	m = len(n)
	for i in range(0,m-1):
		if n[i] > n[i+1]:
			return False
	return True
AAA = list(map(int, input().split()))
if otra(AAA):
	print("ORDENADA")
else:
	print("DESORDENADA")
