# Ejercicio 43: El CIF de la empresa, versión corta (Olimpiada de Tenerife 2026, ejercicio 3)
# Igual que el 42, pero la tabla de letras se hace con "JABCDEFGHI"[numero] en vez de elif.
# Ejemplo: A4233456 → A42334565 | Q1234567 → Q1234567D

import sys
def resultado(R):
	par = 0
	impar = 0
	posicion = len(R)
	for i in range(0,posicion):
		if i % 2 != 0 :
			par = par + int(R[i])
		else:
			impa = int(R[i]) * 2
			if impa < 10:
				impar = impar + impa
			else:
				impadividido = impa // 10
				restoimpa = impa % 10
				ya = impadividido + restoimpa
				impar = impar + ya
	suma = par + impar
	casi = suma % 10
	control = (10 - casi) % 10
	uwu = str(control)
	return uwu
for linea in sys.stdin:
	n = str(linea.strip())
	m = n[1 : 9]
	rr = resultado(m)
	if n[0] in "NPQRSW":
		n = n + "JABCDEFGHI"[int(rr)]
	else:
		n = n + rr
	print(str(n))
