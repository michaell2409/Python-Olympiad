# Ejercicio 41: Primos entre dos números
# Lee A y B e imprime todos los primos entre A y B, ambos incluidos.
# Ejemplo: 10 30 → 11 13 17 19 23 29 | 2 10 → 2 3 5 7
# Idea: esprimo sale con return False en cuanto encuentra un divisor.

def esprimo(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True	
naranjo = list(map(int, input().split()))
jugo = []
for naranjas in range(naranjo[0],naranjo[1]+1):
	if esprimo(naranjas)  and naranjas >= 2:
		jugo.append(naranjas)
print(*jugo)
