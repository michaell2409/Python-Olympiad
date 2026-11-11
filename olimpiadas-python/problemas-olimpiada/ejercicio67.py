# Ejercicio 67: Calculadora de Edad (Olimpiada de Las Palmas 2025, ejercicio 1)
# Lee un año de nacimiento, calcula la edad en 2025 y dice si es mayor o menor de edad.
# Imprime ERROR si no es un año válido, si la edad es mayor de 110 o si es 0 o menos.
# Ejemplo: 2015 → 10 / Menor de edad | 2054 → ERROR | xucb → ERROR
# Tiempo: 13 minutos, sin pistas

lista = list(input().split())
if len(lista) == 1 and lista[0].isdigit() and len(lista[0]) == 4:
	nacimiento = lista[0] 
	resultado = 2025 - int(nacimiento)
	if resultado > 110 or resultado <= 0:
		print("ERROR")
	elif resultado < 18:
		print(resultado)
		print("Menor de edad")
	else:
		print(resultado)
		print("Mayor de edad")
else:
	print("ERROR")
