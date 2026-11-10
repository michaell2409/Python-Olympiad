# Ejercicio 61: Watermelon (Codeforces 4A) - Accepted
# https://codeforces.com/problemset/problem/4/A
# Dificultad en Codeforces: 800 (la más baja de la escala, que va de 800 a 3500)
# Lee el peso w de una sandía e imprime YES si se puede partir en dos trozos pares (cada uno con peso positivo), o NO.
# Ejemplo: 8 → YES | 2 → NO | 5 → NO
# Idea: tiene que ser par y mayor que 2 (con 2 los trozos serían 1 y 1, que son impares).

w = int(input())
if w < 3:
    print("NO")
elif w % 2 == 0:
    print("YES")
else:
    print("NO")
