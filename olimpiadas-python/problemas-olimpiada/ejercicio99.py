# Ejercicio 99: Baldosas (Olimpiada de Las Palmas 2023, ejercicio 4)
# Calcula el lado de la baldosa cuadrada más grande (entre 5 y 70 cm) que cabe exacta en las dos medidas.
# Idea mía: probar desde 70 hacia abajo y quedarme con la primera que divide a las dos.
# Si ninguna entre 5 y 70 sirve → FUERA DE RANGO. Leo con sys.stdin.read().split() (una o dos líneas).
# Ejemplo: 670 800 → 10 | 425 315 → 5 | 450,6 23 → ERROR
# Tiempo: 35 minutos

import sys
dato = sys.stdin.read().split()
contador = 0 
if len(dato) == 2 and all(p.isdigit() for p in dato) and all(p.isascii() for p in dato):
	dato[0] = int(dato[0])
	dato[1] = int(dato[1])
	for i in range(70, 4, -1):
		if dato[0] % i == 0 and dato[1] % i == 0:
			resulatado = i
			print(resulatado)
			contador = contador + 1 
			exit() 
	if contador == 0:  	 
		print("FUERA DE RANGO")	

else:
	print("ERROR")
