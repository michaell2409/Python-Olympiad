# Ejercicio 20: Suma y cantidad
# Lee una línea con varios números e imprime la suma y cuántos hay.
# Ejemplo: 3 7 1 9 4 → 24 5
# Lección 4: listas y textos

numeros = list(map(int, input().split()))
print (sum(numeros), len(numeros))
