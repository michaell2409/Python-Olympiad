# Ejercicio 48: La entrada del cine (repaso: condiciones)
# Lee una edad e imprime el precio: menores de 12 → 5, de 12 a 64 → 9, 65 o más → 6.
# Ejemplo: 8 → 5 | 12 → 9 | 65 → 6

edad = int(input())
if edad < 12:
	print(5)
elif edad < 65:
	print(9)
else:
	print(6)
