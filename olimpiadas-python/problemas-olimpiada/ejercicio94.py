# Ejercicio 94: Secuencias balanceadas (Olimpiada de Las Palmas 2025, ejercicio 4) - MI PRIMERA RECURSIÓN EN UN P4
# Genera todas las secuencias de n pares de paréntesis balanceadas, en orden. ERROR si n no es un entero de 1 a 10.
# Idea: voy añadiendo carácter a carácter. Puedo poner "(" si llevo menos de n,
# y puedo poner ")" si hay más abiertos que cerrados. Probando primero "(" salen ordenadas.
# Ejemplo: 3 → ((())) / (()()) / (())() / ()(()) / ()()()
# Tiempo: 1 hora y 38 minutos (con los ejercicios 90-93 de práctica antes)

n = input().split()
n = input().split()
texto = ""
if len(n) > 0 and n[0].isdigit() and  n[0].isascii() and  1<= int(n[0]) <= 10  and  len(n) == 1 :
	n = int(n[0])
	def parentesis(texto, n):
		if len(texto) == (n*2):
			print(texto)
		
		else:
			abiertos = texto.count("(")
			cerados = texto.count(")")
			
			if abiertos < n:  
				parentesis(texto + "(", n)
			if abiertos - cerados > 0:   		
				parentesis(texto + ")" , n)
						

	parentesis(texto, n)

else:
	print("ERROR")
