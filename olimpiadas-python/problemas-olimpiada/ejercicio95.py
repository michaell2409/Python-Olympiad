# Ejercicio 95: Calculadora (Olimpiada de Las Palmas 2023, ejercicio 1)
# Opera dos enteros (+, -, *, /). La división muestra el cociente sin decimales; dividir entre 0 da ERROR.
# Aprendido: isdigit() no acepta negativos (uso lstrip("-")) y // redondea hacia abajo con negativos (uso int(a / b)).
# Ejemplo: -10 -33 - → 23 | 1 3 / → 0 | -80 0 / → ERROR
# Tiempo: 27 minutos

numeros = input().split()
if len(numeros) > 0 and len(numeros) == 3 and "--" not in numeros[0] and "--" not in numeros[1] and numeros[0].lstrip("-").isdigit() and numeros[1].lstrip("-").isdigit() and (numeros[2] == "+" or numeros[2] == "*" or numeros[2] == "-" or numeros[2] == "/" ):
	
	if numeros[2] == "+":
		resultado = int(numeros[0]) + int(numeros[1])

	elif numeros[2] == "-":

		resultado = int(numeros[0]) - int(numeros[1])



	elif numeros[2] == "*":
		resultado = int(numeros[0]) * int(numeros[1])

	elif numeros[2] == "/":
		if int(numeros[1]) == 0:
			print("ERROR")
			exit()
		resultado = int(int(numeros[0]) / int(numeros[1]))
	print(resultado)
			

else:
	print("ERROR")
