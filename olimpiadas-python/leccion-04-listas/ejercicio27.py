# Ejercicio 27: Vecinos
# Cuenta cuántas veces un número es mayor que el que tiene justo delante.
# Ejemplo: 1 5 3 4 8 2 → 3
# Idea: Comparo cada número con el siguiente y paro en u-1 para no salirme de la lista.

numero = list(map(int, input().split()))
u = len(numero)
contador = 0
for i in range(0,(u-1)):
	if numero[i] < numero[(i+1)]:
		contador = contador + 1 
print(contador)
