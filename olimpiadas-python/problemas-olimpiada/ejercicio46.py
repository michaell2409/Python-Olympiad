# Ejercicio 46: Números romanos, parte A sin restas: romano → decimal (Olimpiada de Tenerife 2026, ejercicio 4)
# Lee un número romano y suma el valor de cada letra.
# Ejemplo: LVIII → 58 | XX → 20 | MDCLXVI → 1666
# Pendiente: añadir la regla de restar (con XIV todavía da 16 en vez de 14).

dicionario = {"M":1000, "CM":int(900), "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
e = int() 
m = input()
for a in m:
	for z in dicionario:
		if a == z:
			e = e + dicionario[z] 
print(e)
