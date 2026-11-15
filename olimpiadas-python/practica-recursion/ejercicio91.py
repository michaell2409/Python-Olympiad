# Ejercicio 91: Todos los códigos binarios (práctica de recursión)
# Genera todas las combinaciones de n cifras con 0 y 1, en orden, con recursión.
# Aprendido: en cada paso se llama una vez por cada opción, y el orden de las llamadas decide el orden de la salida.
# Ejemplo: 2 → 00 / 01 / 10 / 11
# Tiempo: 10 minutos

n = int(input())
texto = ""
def combinaciones(texto, n):
	
	if len(texto) == n:
		print(texto)
	else:
		combinaciones((texto + "0"), n)
		combinaciones((texto + "1"), n)
combinaciones(texto, n)
