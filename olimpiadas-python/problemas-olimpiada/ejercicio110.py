# Ejercicio 110: Los números amigos de Aday (IV Olimpiada Informática de Tenerife 2026, P2)
# Por cada par A B dice si son números amigos (la suma de los divisores propios de cada uno es el otro).
# Busca los divisores por parejas (c y n//c) solo hasta c*c <= n para que sea rápido.
# Ejemplo: 220 284 → AMIGOS | 100 200 → NO AMIGOS
# Tiempo: 8 minutos la primera versión (lenta) y 35 minutos en total aprendiendo el truco de las parejas de divisores

import sys 
for linea in sys.stdin:
	listaa = [1]
	listab = [1]
	a, b = map(int, linea.split())
	c = 2
	while c * c <= a:
		if a % c == 0:
			listaa.append(c)
			if c != a // c:
				listaa.append(a//c) 
		c = c + 1 	     
	c = 2
	while c * c <= b:
		if b % c == 0:
			listab.append(c)
			if c != b //c:
				listab.append(b//c)
		c = c + 1
	if a == 1 and b == 1:
		print("AMIGOS") 		

	elif sum(listaa) == b and sum(listab) == a:
		print("AMIGOS") 
	else:
		print("NO AMIGOS")
