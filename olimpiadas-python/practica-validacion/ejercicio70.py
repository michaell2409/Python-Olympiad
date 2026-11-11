# Ejercicio 70: Fecha DD/MM/AAAA (práctica de validación)
# Comprueba que la fecha tenga el formato DD/MM/AAAA, día 01-31, mes 01-12 y año 1900-2100.
# Ejemplo: 05/11/2026 → VALIDA | 5/11/2026 → ERROR | 32/01/2020 → ERROR
# Tiempo: 20 minutos

fecha = input().split("/")
if len(fecha) == 3 and fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit() and len(fecha[0]) == 2 and len(fecha[1]) == 2 and len(fecha[2]) == 4 and int(fecha[0]) > 0 and int(fecha[1]) > 0 \
and int(fecha[0]) < 32 and int(fecha[1]) < 13 and int(fecha[2]) > 1899 and int(fecha[2]) < 2101:
	print("VALIDA")
else:
	print("ERROR")
