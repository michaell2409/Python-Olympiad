# Ejercicio 58: El compresor completo (Olimpiada de Tenerife 2026, ejercicio 5)
# Cada caso son dos líneas: la operación (C comprimir, D descomprimir) y el texto.
# Imprime ERROR si la operación no es C ni D, si al comprimir hay algo que no son minúsculas,
# o si al descomprimir el formato está roto (a una letra le falta su número, o son todo cifras).
# Ejemplo: C aaabbbccc → a3b3c3 | D a3b12 → aaabbbbbbbbbbbb | D ab3 → ERROR

def comprimir(n):
	x = n + str(111111)
	q = len(x)
	lista = []
	resultado = ""
	contador = 1 
	for i in range(0, q-1):
		if x[i] == x[i+1]:
			contador = contador + 1  
		elif x[i] != x[i+1]:
			lista.append(x[i])
			lista.append(contador)
			contador = 1 
	for W in lista:
		resultado = resultado + str(W)
	return(resultado)



def descomprrimir(n):
	resultado = ""
	for i in range(0, len(n)):
		if not n[i].isdigit():
			letrica = n[i]
			numero = ""
			j = i + 1
			while j < len(n) and n[j].isdigit():
				numero = numero + n[j]
				j = j + 1
			if numero == "":
				return "ERROR"	
			resultado = resultado + letrica * int(numero)
	return(resultado)





import sys
lineas = sys.stdin.read().split()
for i in range(0, len(lineas), 2):
	if lineas[i] == "C":
		if lineas[i+1].isalpha() and lineas[i+1].islower(): 
			print(comprimir(lineas[i+1]))
		else:
			print("ERROR")

	elif lineas[i] == "D":
		if lineas[i+1].isdigit():
			print("ERROR")	
		else:
			print(descomprrimir(lineas[i+1]))
	else:
		print("ERROR")
