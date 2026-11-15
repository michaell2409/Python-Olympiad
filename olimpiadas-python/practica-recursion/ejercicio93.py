# Ejercicio 93: Sin dos unos seguidos, versión 2 (práctica de recursión)
# Lo mismo que el 92, pero sin ir nunca por los caminos prohibidos:
# solo añado un "1" si el texto está vacío o no termina en "1". Es más rápido.
# Ejemplo: 3 → 000 / 001 / 010 / 100 / 101
# Tiempo: 7 minutos

n = int(input())
texto = ""
def combinaciones(texto, n):
	
	if len(texto) == n :
		print(texto)
	else:
		combinaciones((texto + "0"), n)
		if len(texto) > 0 and  texto[-1] == "1":
			pass
		else:

			combinaciones((texto + "1"), n)
combinaciones(texto, n)
