# Ejercicio 92: Sin dos unos seguidos, versión 1 (práctica de recursión)
# Genera las combinaciones de n cifras con 0 y 1 sin dos 1 seguidos.
# En esta versión genero todas y al final descarto las que tienen "11".
# Ejemplo: 3 → 000 / 001 / 010 / 100 / 101
# Tiempo: 6 minutos

n = int(input())
texto = ""
def combinaciones(texto, n):
	
	if len(texto) == n:
		if "11" in texto:
			pass
		else:
			print(texto)
	else:
		combinaciones((texto + "0"), n)
		combinaciones((texto + "1"), n)
combinaciones(texto, n)
