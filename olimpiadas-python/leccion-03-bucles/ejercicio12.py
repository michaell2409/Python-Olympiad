# Ejercicio 12: Cuenta atrás de Collatz
# Lee un número N. Mientras no sea 1: si es par, lo divide entre 2;
# si es impar, lo multiplica por 3 y le suma 1. Imprime cuántos pasos hace.
# Ejemplo: entrada 6 → salida 8 | entrada 27 → salida 111 | entrada 1 → salida 0

n = int(input())
suma = 0
while n != 1 :
     suma = suma + 1 
     if n % 2 == 0:
         n = n // 2 
        

     else: 
         n = n * 3 + 1 
        

print(suma)
