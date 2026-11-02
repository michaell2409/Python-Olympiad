# Ejercicio 29: Sin repetidos
# Imprime los números de la lista sin repetir, en el orden en que aparecen por primera vez.
# Ejemplo: 4 2 4 7 2 9 4 → 4 2 7 9

lista = list(map(int, input().split()))
resultado = []
for i in lista:
	if i in resultado:
		pass
	else: 
		resultado.append(i)
print(*resultado)
