# Ejercicio 82: Código de producto (práctica de validación)
# Comprueba que un código tenga el formato AAA-9999-A (mayúsculas A-Z, cifras) y que el número esté entre 0001 y 5000.
# Ejemplo: ABC-1234-X → VALIDO | abc-1234-X → ERROR | ABC-0000-X → ERROR
# Tiempo: 28 minutos

import string
codigo = input().split("-")
permitidas =  string.ascii_uppercase
if len(codigo) == 3 and len(codigo[0]) == 3 and len(codigo[1]) == 4 and len(codigo[2]) == 1  and  all( p in permitidas and codigo[2] in permitidas for p in codigo[0]) \
and codigo[1].isdigit() and codigo[1].isascii() and int(codigo[1]) < 5001 and int(codigo[1]) > 0:
	print("VALIDO")
else:
	print("ERROR")	
