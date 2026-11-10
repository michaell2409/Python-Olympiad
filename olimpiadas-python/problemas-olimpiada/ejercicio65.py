# Ejercicio 65: Calculando el IMEI (Olimpiada de Tenerife 2025, ejercicio 1)
# Para cada línea con los 14 primeros dígitos de un IMEI, imprime el IMEI completo con su dígito de control.
# Ejemplo: 49015420323751 → 490154203237518
# Idea: algoritmo de Luhn, el mismo tipo de cálculo que el CIF. Resuelto sin pistas en 41 minutos.

import sys 
for linea in sys.stdin:
	n = linea.strip()
	numerosimpares = 0 
	numerospares = 0 
	numeros = 0 
	control = 0
	for i in range(0, len(n)):
		if i % 2 != 0:
			q = int(n[i])
			w = q * 2
			if w >= 10:
				e = w % 10
				r = w // 10
				t = e + r 
				numerosimpares = numerosimpares + t 
			else: 
				numerosimpares = numerosimpares + w	       
		else:
			y = int(n[i])
			numerospares = numerospares + y
		numeros = numerosimpares + numerospares
	if numeros % 10 != 0:
		l = numeros // 10
		control = ((l*10)+10) - numeros     

	print(n + str(control))
