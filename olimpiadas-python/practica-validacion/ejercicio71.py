# Ejercicio 71: Matrícula (práctica de validación)
# Matrícula española: 4 dígitos, un espacio y 3 letras mayúsculas sin vocales ni Q.
# Ejemplo: 1234 BCD → VALIDA | 1234 BCA → ERROR | 1234 bcd → ERROR
# Tiempo: 40 minutos

import string
matricula = input()
q = matricula[:4] + matricula[5:]
contador = 0
nopermitidas = string.ascii_lowercase +"AEIOUQ"  
if len(matricula) == 8 and matricula[4] == " " and matricula[:4].isdigit() and matricula[5:].isalpha() and matricula[5:].isascii() and matricula[5:].isupper():
	for i in q:
		if i in nopermitidas:
			contador = contador + 1 
else:
	contador = contador + 1
if contador == 0:
	print("VALIDA")
else:
	print("ERROR")
