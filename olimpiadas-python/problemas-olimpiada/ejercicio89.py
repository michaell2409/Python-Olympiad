# Ejercicio 89: Códigos Perdidos (Olimpiada de Las Palmas 2024, ejercicio 4)
# Si el número es primo, lo devuelve. Si no, prueba a añadir una cifra del 1 al 9 a la derecha,
# a la izquierda o a los dos lados, y devuelve el primo más pequeño (o NO RECONSTRUIBLE).
# Aprendido: comprobar si es primo probando divisores solo mientras e * e <= numero, y el break.
# Ejemplo: 3431 → 23431 | 20 → 1201 | 109947 → NO RECONSTRUIBLE
# Tiempo: 2 horas y 27 minutos

numero = input()
contador = 0 
listilla = []
resultado = []
contador1 = 0
e = 2 
if len(numero) > 0 and numero.isdigit() and numero.isascii() and int(numero) != 0 and int(numero) != 1:
	
	while e*e <= int(numero):
		if  int(numero) % e == 0:
			contador = contador + 1
		e = e + 1 
				 
	if contador == 0:
		print(numero)
	else:
		for i in range(1, 10):
			numero1 = numero + str(i)
			listilla.append(numero1)
			numero2 = str(i) + numero
			listilla.append(numero2)
			for w in range(1,10):
				numero3 = str(i) + numero + str(w)
				listilla.append(numero3) 
		listilla = [int(x) for x in listilla]
		listilla = sorted(listilla)
		for i in listilla:
			E = 2
			while E * E <= i: 
				if i % E == 0:
					contador1  = contador1 + 1
					break
				E = E +1
			if contador1 == 0:
				resultado.append(i)		 
			else:
				contador1 = 0
		if len(resultado) == 0:
			print("NO RECONSTRUIBLE")
		else:
			print(resultado[0])			 

elif numero == "1":
	print(11) 

else:
	print("ERROR")
