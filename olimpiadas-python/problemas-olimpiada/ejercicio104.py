# Ejercicio 104: Verificación en la empresa (I Olimpiada Informática de Tenerife 2023, P1)
# Por cada línea con un código (mayúscula + 7 cifras) calcula la letra de control con los pesos
# 1,4,2,3,9,7,1 y la tabla XDFPLMTHAE; si el código no es válido muestra ERROR y sigue.
# Ejemplo: S4785112 → S4785112D | 4785112S → ERROR
# Tiempo: 48 minutos

import sys
import string
orden = [1,4,2,3,9,7,1]

letras = "XDFPLMTHAE" 
for linea in sys.stdin:
	linea = linea.strip("\n")
	if len(linea) == 8 and linea[0] in string.ascii_uppercase and all(linea[p].isdigit() and linea[p].isascii() for p in range(1,8)):
		lista = []
		for i in range(len(orden)):
			lista.append(orden[i] * int(linea[i+1]))
		
		
		resto = sum(lista) %	10
		linea = linea + letras[resto]
		print(linea)


	
	else:
		print("ERROR")
