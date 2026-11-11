# Ejercicio 72: Suma estricta (práctica de validación)
# Suma números enteros de 0 a 1000 separados por un solo espacio.
# Imprime ERROR si está vacía, hay espacios sobrantes, algo que no sea número o un número fuera de rango.
# Ejemplo: 10 20 30 → 60 | 10  20 → ERROR | 5 -3 → ERROR
# Tiempo: 35 minutos

numeros = input()
numerito = map(int, numeros.split())
resultado = numeros.split()
contador = 0 
numerotes = ""
ya = 0
for r in numeros:
	if r != " ":
		numerotes = numerotes + r 
if len(numeros) > 0 and numerotes.isdigit() and  numeros[0] != " " and numeros[-1] != " " and "  " not in numeros: 
	for i in numerito:
		if i > 1000 or i < 0:
			contador = contador + 1
else:
	contador = contador + 1 
if contador == 0:
	for o in resultado:
		ya = ya + int(o)
	print(ya)	
else:
	print("ERROR")
