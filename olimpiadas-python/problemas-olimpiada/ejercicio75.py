# Ejercicio 75: Cinta Bifrontal (Olimpiada de Las Palmas 2026, ejercicio 3)
# Simula una cinta: con L se coge la letra de la izquierda de la bobina S y se pone a la izquierda de la cinta;
# con R se coge la de la derecha y se pone a la derecha. ERROR si S no es a-z, T no es L/R, longitudes distintas, n = 0 o n > 20000.
# Ejemplo: abcd + LRRL → badc
# Tiempo: 1 hora y 28 minutos (mi primer P3)

import string
s = input()
t = input()
resultado = []
contador = 0 
def espacios(m):
	if m[0] != " " and m[-1] != " ":
		return(True)

if len(s) == len(t) and len(s) > 0 and len(t) <= 20000 and espacios(s) and espacios(t):
	for i in s:
		if i not in string.ascii_lowercase:
			contador = contador + 1  
	for q in t:
		if q not in "LR":
			contador = contador + 1
	e = t
	y = list(s.strip())
	for r in e:
		if r == "L":
			resultado = resultado[::-1] 
			resultado.append(y[0])
			resultado = resultado[::-1]
			y.pop(0)	
		elif r == "R":
			resultado.append(y[-1])
			y.pop(-1)
else:
	contador = contador +1	
if contador == 0:
	print(*resultado, sep="")
else:
	print("ERROR")
