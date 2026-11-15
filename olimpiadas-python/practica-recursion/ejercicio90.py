# Ejercicio 90: Factorial recursivo (práctica de recursión)
# Calcula n! con una función que se llama a sí misma, sin for ni while.
# Aprendido: caso base (n == 1) + caso recursivo (n * factorial(n - 1)); return termina la función.
# Ejemplo: 5 → 120
# Tiempo: 4 minutos

n = int(input())
def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n-1)
print(factorial(n))
