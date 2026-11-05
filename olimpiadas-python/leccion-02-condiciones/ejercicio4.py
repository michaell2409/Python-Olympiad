# Ejercicio 4: Par o impar
# Lee un número e imprime si es par o impar.
# Ejemplo: 13 → IMPAR | 8 → PAR
# Lección 2: condiciones (if, elif, else)

numero = int(input())
v1 = numero % 2 
if v1 == 0: 
    print("par")
else: 
    print("impar")
