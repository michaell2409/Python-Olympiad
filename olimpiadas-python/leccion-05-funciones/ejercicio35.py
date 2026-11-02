# Ejercicio 35: Múltiplos de 7
# Función es_multiplo_7(n) que devuelve True/False; cuenta los múltiplos de 7 de una lista.
# Ejemplo: 7 10 14 3 21 → 3

def es_multiplo_7(n):
	return n % 7 == 0 
numeros = list(map(int, input().split()))
contador = 0
for i in numeros:
	if es_multiplo_7(i):
		contador = contador + 1 

print(contador)
