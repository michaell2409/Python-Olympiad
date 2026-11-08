# Ejercicio 55: ¿Cuánto mide cada grupo? (puente hacia el compresor)
# Lee una palabra e imprime el tamaño de cada grupo de letras seguidas iguales.
# Ejemplo: aaabbc → 3 2 1 | aaabaa → 3 1 2 | zzzz → 4
# Idea: centinela. Pego 1s al final para que el último grupo también termine con un cambio y se guarde.

m = input()
x = m + str(111111)
q = len(x)
lista = []
contador = 1 
for i in range(0, q-1):
    if x[i] == x[i+1]:
        contador = contador + 1  
    elif x[i] != x[i+1]:
        lista.append(contador)
        contador = 1 
print(*lista)
