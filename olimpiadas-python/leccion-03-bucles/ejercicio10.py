# Ejercicio 10: La tabla de multiplicar
# Lee un número e imprime su tabla del 1 al 10 con el formato "7 x 1 = 7".
# Ejemplo: entrada 7 → salida 7 x 1 = 7 ... 7 x 10 = 70

n = int(input())
for i in range (1 , 11):
    m = (n * i)
    print (f"{n} x {i} = {m}")
