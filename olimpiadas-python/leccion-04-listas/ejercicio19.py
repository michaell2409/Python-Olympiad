# Ejercicio 19: El mayor y el menor
# Lee una línea con varios números e imprime el mayor y el menor.
# Ejemplo: 3 7 1 9 4 → 9 1
# Lección 4: listas y textos

n = list(map(int,input().split()))
print (max(n),  min(n))
