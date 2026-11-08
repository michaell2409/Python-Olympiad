# Ejercicio 54: ¿Cuántos grupos? (puente hacia el compresor)
# Lee una palabra e imprime cuántos grupos de letras seguidas iguales tiene.
# Ejemplo: aaabbc → 3 | aabaa → 3 | zzzz → 1
# Idea: el contador empieza en 1 (el primer grupo) y suma 1 cada vez que la letra cambia.

m = input()
q = len(m)
z = m + m[q-1]
contador = 1 
for i in range(0,q-1):
    if z[i] != z[i+1]:
        contador = contador + 1
print(contador)
