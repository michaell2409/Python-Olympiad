# Ejercicio 31: El mayor de tres
# Función que devuelve el mayor de tres números sin usar max.
# Ejemplo: 4 9 2 → 9 | 5 5 2 → 5
# Idea: Uso >= para que funcione también con empates.

def numeros(a, b, c):
	if a >= b and a >= c: 
		return(a)
	elif b >= a and b >= c: 
		return(b)
	elif c >= a and c >= b: 
		return(c)

numeritos = list(map(int, input().split()))
print(numeros(numeritos[0], numeritos[1], numeritos[2]))
