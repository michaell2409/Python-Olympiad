# Ejercicio 49: Suma de los pares (repaso: bucles)
# Lee N e imprime la suma de los números pares del 1 al N.
# Ejemplo: 10 → 30 | 7 → 12 | 1 → 0

n = int(input())
hucha = 0 
for i in range(n+1): 
	if i % 2 == 0:
		hucha = hucha + i  	
print(hucha)
