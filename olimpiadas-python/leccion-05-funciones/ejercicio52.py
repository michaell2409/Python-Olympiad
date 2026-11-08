# Ejercicio 52: Múltiplos de 3 o de 5 (repaso: funciones)
# Función especial(n) que dice si n es múltiplo de 3 o de 5; cuenta los especiales del 1 al N.
# Ejemplo: 10 → 5 | 15 → 7 | 2 → 0

def especial(n):
    if n % 3 == 0 or n % 5 == 0:  
        return True
    return False        # True si n es múltiplo de 3 o de 5

m = int(input())
contador = 0
for i in range(1,m+1):
    if especial(i):
        contador = contador + 1
print(contador)
