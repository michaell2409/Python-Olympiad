# Ejercicio 73: Cadenas con Intercambio de Dígitos (Olimpiada de Las Palmas 2025, ejercicio 2)
# A cada dígito le suma 7 y se queda con la última cifra ((d + 7) % 10), y luego le da la vuelta a la cadena.
# Imprime ERROR si hay algo que no sea dígito, está vacía o pasa de 100 cifras.
# Ejemplo: 972787 → 454946
# Tiempo: 25 minutos, sin pistas

cadena = input()
resultado = []
if cadena.isdigit() and len(cadena) <= 100:
	for i in cadena:
		i = int(i)
		q = (i + 7) % 10
		resultado.append(q)
	print(*resultado[::-1], sep="")
else:
	print("ERROR")
