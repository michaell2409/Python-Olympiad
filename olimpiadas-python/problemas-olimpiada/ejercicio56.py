# Ejercicio 56: El compresor, parte de comprimir (Olimpiada de Tenerife 2026, ejercicio 5)
# Lee una palabra y escribe cada grupo de letras seguidas con su letra y cuántas veces se repite.
# Ejemplo: aaabbbccc → a3b3c3 | aabaa → a2b1a2 | x → x1
# Idea: centinela de 1s al final para cerrar el último grupo; imprimo la lista sin espacios con sep="".
# Pendiente: descomprimir y detectar entradas incorrectas.

m = input()
x = m + str(111111)
q = len(x)
lista = []
contador = 1 
for i in range(0, q-1):
    if x[i] == x[i+1]:
        contador = contador + 1  
    elif x[i] != x[i+1]:
        lista.append(x[i])
        lista.append(contador)
        contador = 1 
print(*lista, sep="")
