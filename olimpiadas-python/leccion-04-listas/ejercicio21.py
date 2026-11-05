# Ejercicio 21: Al revés
# Lee una línea con varios números y los imprime en orden inverso.
# Ejemplo: 1 2 3 4 5 → 5 4 3 2 1
# Idea: recorro las posiciones desde la última (len-1) hasta la 0.
# Lección 4: listas y textos

lista = list(map(int, input().split()))
otro = []
u = (len(lista))
for m in range(u-1,-1,-1):
	otro.append(lista[m])
print(*otro)
