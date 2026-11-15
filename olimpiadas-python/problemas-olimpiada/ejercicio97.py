# Ejercicio 97: Quinta sucesora, versión 2 (Olimpiada de Las Palmas 2023, ejercicio 2)
# Lo mismo que el 96, pero creando el alfabeto con string.ascii_lowercase y metiendo la ñ en la posición 14:
# letras[:14] + "ñ" + letras[14:]. Como es un texto, compruebo además que sea una sola letra.
# Ejemplo: h → m | X → c | { → ERROR
# Tiempo: 7 minutos

import string
letra = input().split()
abecedario = string.ascii_lowercase
abecedario = abecedario[:14] + "ñ" + abecedario[14:]
abecedario = abecedario + abecedario
if len(letra) == 1 and len(letra[0]) == 1 and letra[0].lower() in abecedario:
	resultado = abecedario.index(letra[0].lower())
	print(abecedario[resultado+5])
else:
	print("ERROR")
