# Ejercicio 22: Contar vocales
# Lee una palabra en minúsculas e imprime cuántas vocales tiene.
# Ejemplo: olimpiada → 5 | python → 1

palabra = str(input())
u = (len(palabra))
contador = 0 
for i in range(0,u):

	if (palabra[i])  in "aeiou":
		contador = contador + 1
	else:
		continue	
print(contador)
