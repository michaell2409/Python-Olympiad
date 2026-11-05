# Ejercicio 5: El mayor de dos
# Lee dos números e imprime el mayor, o IGUALES si son iguales.
# Ejemplo: 4 9 → 9 | 7 7 → IGUALES
# Lección 2: condiciones (if, elif, else)

numero1, numero2 = map(int, input().split())
if numero1 > numero2:
	print(numero1)
elif numero1 < numero2:
	print(numero2)
else: 
    print("iguales")