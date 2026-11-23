# Ejercicio 112: Suma de cifras (calentamiento tras el RetoFest)
# Por cada línea con un número entero no negativo muestra la suma de sus cifras;
# si la línea está vacía o tiene algo que no sea una cifra, muestra ERROR y sigue.
# Ejemplo: 123 → 6 | 12a → ERROR
# Tiempo: 12 minutos

import sys 
for linea in sys.stdin:
	resultado = 0
	linea = linea.rstrip("\n")
	if len(linea) > 0 and  linea.isdigit() and linea.isascii() and all(p not in  " " for p in linea):

		for i in linea:
			i = int(i)
			resultado = resultado + i
		print(resultado)		 



	else:
		print("ERROR")
