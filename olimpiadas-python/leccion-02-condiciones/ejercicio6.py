# Ejercicio 6: Positivo, negativo o cero
# Lee un número e imprime si es positivo, negativo o cero.
# Ejemplo: -5 → NEGATIVO | 0 → CERO
# Lección 2: condiciones (if, elif, else)

numero = int(input())
if numero > 0:
	print("positivo")
elif numero < 0:
	print("negativo")
else: 
	print("cero")