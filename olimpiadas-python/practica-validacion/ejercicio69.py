# Ejercicio 69: Nombre de usuario (práctica de validación)
# Un nombre de usuario es VALIDO si tiene de 3 a 15 caracteres, solo minúsculas a-z, dígitos o "_",
# y no empieza por dígito. Si no, ERROR.
# Ejemplo: mike_24 → VALIDO | 2mike → ERROR | Mike → ERROR
# Tiempo: 1 hora

import string 
nombre = input()
permitidos = string.ascii_lowercase + "_" + string.digits
contador = 0
contador1 = 0 
if len(nombre) > 2 and len(nombre) < 16 and not nombre[0].isdigit():
	for i in nombre:
		if i not in permitidos:
			print("ERROR")
			contador1 = contador1 + 1
			break 
		else:
			contador = contador + 1 	
		
else:
	print("ERROR")
if contador > 1 and contador1 == 0: 
	print("VALIDO")
