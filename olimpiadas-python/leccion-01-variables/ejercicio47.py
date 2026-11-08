# Ejercicio 47: Horas y minutos (repaso: variables y operaciones)
# Lee un número de minutos e imprime cuántas horas y minutos son.
# Ejemplo: 135 → 2 15 | 60 → 1 0 | 45 → 0 45

minutos = int(input())
horas = minutos // 60
sobras = minutos % 60  
print(f"{horas} {sobras}")
