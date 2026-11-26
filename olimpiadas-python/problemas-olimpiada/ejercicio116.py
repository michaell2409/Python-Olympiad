# Ejercicio 116: El CIF de la empresa (IV Olimpiada Informática de Tenerife 2026, P3)
# Calcula el dígito de control de cada CIF: dobla las cifras en posición impar (sumando sus dígitos si pasa de 9),
# suma las pares, control = (10 - unidad) mod 10; si la letra es N, P, Q, R, S o W el control va en letra (JABCDEFGHI).
# Ejemplo: A4233456 → A42334565 | Q1234567 → Q1234567D
# Tiempo: 37 minutos

import sys
linea = sys.stdin
for i in linea:
	r = 0
	w = 0
	t = 0
	control = "JABCDEFGHI"
	i = i.rstrip("\n")
	linea1 = i[1:]
	for e in range(0, len(linea1), 2):

		q = int(linea1[e]) * 2
		if q > 9:
			q = q%10 + q//10
		w = w + q 	
	
	for e in range(1, len(linea1), 2):
		
		r = r + int(linea1[e])	
	t = (10 - ((r + w)%10))%10
	if i[0] == "N" or i[0] == "P" or i[0] == "Q" or i[0] == "R" or i[0] == "S" or i[0] == "W":
		i = i + control[t]
		print(i)
	else:
		t = str(t)
		i = i + t
		print(i)
