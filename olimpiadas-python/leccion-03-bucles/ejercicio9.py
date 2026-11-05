# Ejercicio 9: Suma del 1 al N
# Lee un número N e imprime la suma 1 + 2 + ... + N.
# Ejemplo: entrada 5 → salida 15 | entrada 100 → salida 5050
#
# Mi idea: n ya empieza valiendo el propio número,
# así que solo me falta sumarle del 1 al n-1.
# range(1, n) se calcula una sola vez al principio,
# por eso no cambia aunque n cambie dentro del bucle.

n = int(input())
for i in range(1, n):
    n = n + i
print(n)
