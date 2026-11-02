# Ejercicio 32: Contar vocales con función
# Función que cuenta las vocales (mayúsculas y minúsculas) de una palabra.
# Ejemplo: olimpiada → 5 | python → 1

def es_vocal(letra):
	vocales = 0 
	for i in letra:
		if i in "aeiouAEIOU":
			vocales = vocales + 1
	return vocales
m = input()
print(es_vocal(m))
