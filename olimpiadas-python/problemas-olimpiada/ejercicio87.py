# Ejercicio 87: Traductor Intergaláctico (Olimpiada de Las Palmas 2024, ejercicio 2)
# Traduce una frase al idioma Azul ("azulo", resto entre 5) o Verde ("verdosu", resto entre 7):
# cada letra -> su posición en el alfabeto -> alfabeto_alien[pos % tamaño]. Los espacios se mantienen.
# ERROR si no empieza por "A " o "V " o si hay algo que no sea letra o espacio.
# Aprendido: .index(), .lower(), recorrer la línea letra a letra para no perder espacios.
# Ejemplo: A hola amigos → uoza aulzol
# Tiempo: 2 horas y 2 minutos

import string
lista =  input()
letras = lista[2:]
letricasminusculas = string.ascii_lowercase 
azul = "azulo"
verde = "verdosu"
resultado = ""
if len(lista) >= 2 and  (lista[0] == "A" or lista[0] == "V") and lista[1] == " " and  all(t in (string.ascii_letters + " ")  for t in letras):
	if lista[0] == "A":
		for i in letras:
			
			if i == " ":
				resultado = resultado + " "
			else:

				e = letricasminusculas.index(i.lower()) % 5
				resultado = resultado + azul[e]
			
	if lista[0] == "V":
		for i in letras:
			
			if i == " ":
				resultado = resultado + " "
			else:

				e = letricasminusculas.index(i.lower()) % 7
				resultado = resultado + verde[e]
			 			 	
	print(resultado)
else:
	print("ERROR")
