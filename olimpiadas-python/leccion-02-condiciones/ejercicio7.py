# Ejercicio 7: ¿Es año bisiesto?
# Lee un año e imprime si es bisiesto.
# Ejemplo: 2024 → SI | 1900 → NO | 2000 → SI
# Lección 2: condiciones (if, elif, else)

año = int(input())
v1 = año % 4
v2 = año % 100 
v3 = año % 400
if ( v1 ==  0 and v2 != 0 ) or v3 == 0:
    print("bisiesto")
else:
    print("no biesto") 