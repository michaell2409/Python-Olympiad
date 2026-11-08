# Ejercicio 51: Aprobados (repaso: listas)
# Lee varias notas e imprime las aprobadas (5 o más) en una línea y cuántas hay en la siguiente.
# Ejemplo: 7 3 5 9 2 10 → 7 5 9 10 / 4

numeros = list(map(int, input().split()))
resultado = 0
lista = []
for i in numeros:
    if i > 4:
        resultado = resultado + 1
        lista.append(i) 
print(*lista)
print(resultado)
