# Ejercicio 44: Precios de una cafetería con diccionario
# Lee el nombre de un producto e imprime su precio, o NO HAY si no está en la carta.
# Ejemplo: cafe → 3 | pizza → NO HAY

dicionario = {"cafe":3, "jugo":2, "carne":4}
n = input()
if n in dicionario:
	print(dicionario[n])
else:
	print("NO HAY")	
