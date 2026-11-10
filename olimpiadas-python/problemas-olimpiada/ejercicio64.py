# Ejercicio 64: Números romanos, romano → decimal con restas (Olimpiada de Tenerife 2026, ejercicio 4)
# Lee un número romano e imprime su valor en decimal.
# Ejemplo: XIV → 14 | MCMXCIV → 1994 | MMMCMXCIX → 3999
# Idea: si una letra vale menos que la de su derecha, se resta; si no, se suma.
# Escrito de memoria en 15 minutos.

dicicionario = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
m = input()
e = 0 
for i in range(len(m)):
	if i < len(m) -1 and dicicionario[m[i]] < dicicionario[m[i+1]]:
		e = e - dicicionario[m[i]]
	else: 
		e = e + dicicionario[m[i]]
print(e)
