# Repaso 2: Suma de cifras
# Lee un número e imprime la suma de sus cifras.
# Ejemplo: 2026 → 10 | 999 → 27
# Idea: % 10 me da la última cifra y // 10 la quita.

n = int(input())
s  = 0
m = 0 
while n != 0:
    m = n % 10
    s = s + m 
    n = n // 10  
print(s)
