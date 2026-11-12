# Ejercicio 74: Segundos del día (práctica de validación)
# Lee una hora HH:MM:SS y dice cuántos segundos han pasado desde las 00:00:00.
# Imprime ERROR si el formato no es exacto o la hora/minutos/segundos están fuera de rango.
# Ejemplo: 10:30:15 → 37815 | 24:00:00 → ERROR | 9:30:15 → ERROR
# Tiempo: 19 minutos

def comparacion(m):
	m = int(m)
	if m < 60:
		return(True)
hora = input().split(":")
if len(hora) == 3 and len(hora[0]) == 2 and len(hora[1]) == 2 and len(hora[2]) == 2 and  hora[0] != " " and hora[2] != " " and "  " not in hora and hora[0].isdigit() and hora[1].isdigit() and hora[2].isdigit() and int(hora[0]) < 24 and comparacion(hora[1]) and comparacion(hora[2]):
	q = int(hora[0]) * 60 * 60
	w = int(hora[1]) * 60
	resultado = q + w + int(hora[2])
	print(resultado)
else:
	print("ERROR")
