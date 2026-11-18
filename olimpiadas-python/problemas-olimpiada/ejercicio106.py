# Ejercicio 106: Juan y los alienígenas (I Olimpiada Informática de Tenerife 2023, P2)
# Por cada línea muestra el mayor producto de tres dígitos consecutivos;
# si tiene menos de tres dígitos o algo que no sea un entero positivo, ERROR.
# Ejemplo: 89763211 → 504 | 75 → ERROR
# Tiempo: 20 minutos

import sys
for entrada in sys.stdin:
	lista = []
	entrada = entrada.rstrip("\n")
	if len(entrada) > 2 and all(p.isdigit() and p.isascii() for p in  entrada):
		for i in range(0, len(entrada)-2):
			lista.append(int(entrada[i])* int(entrada[i+1])* int(entrada[i+2]))
		print(max(lista))	

	
	else:
		print("ERROR")
