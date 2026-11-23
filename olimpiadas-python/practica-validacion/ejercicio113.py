# Ejercicio 113: Palabra capicúa (calentamiento tras el RetoFest)
# Por cada línea con una palabra en minúsculas muestra SI si es capicúa y NO si no;
# si tiene algo que no sea una letra minúscula, muestra ERROR.
# Ejemplo: reconocer → SI | hola → NO | Ana → ERROR
# Tiempo: 12 minutos

import sys
import string
for linea in sys.stdin:
	linea = linea.rstrip("\n") 
	letras = string.ascii_lowercase + "ñ" 
	if len(linea) > 0 and  all(p in letras for p in linea): 
		
		if linea == linea[::-1]:
			print("SI")
		else:
			print("NO")
	else:
		print("ERROR")
