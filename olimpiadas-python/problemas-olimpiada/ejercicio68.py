# Ejercicio 68: Intercambio de Mitades (Olimpiada de Las Palmas 2026, ejercicio 2)
# Lee una frase y a cada palabra le intercambia sus dos mitades (si es impar, la mitad larga es la segunda).
# Imprime ERROR si está vacía, hay espacios al principio/final o dobles, pasa de 100 caracteres o hay algo que no sea letra a-z/A-Z.
# Ejemplo: hola mundo → laho ndomu
# Tiempo: unas 2 horas

frases1 = input()
if len(frases1) ==  0 or frases1[0] == " " or frases1[-1] == " " or "  " in frases1 or len(frases1) > 100:
	print("ERROR")
else:
	frases = frases1.split()	
	resultado = []
	contador = 0
	for e in frases:
		if  not e.isascii() or not e.isalpha():
			contador = contador + 1
	if contador > 0:
		print("ERROR")
	else:
		for i in frases:
			q = len(i) // 2
			w = i[q:] + i[:q]
			resultado.append(w)
		print(*resultado)
