# Repaso 1: Contar dígitos
# Lee un número entero positivo e imprime cuántas cifras tiene.
# Ejemplo: 7 → 1 | 2026 → 4 | 100000 → 6
# Idea: quito cifras con // 10 hasta que no queda ninguna y cuento cuántas he quitado.

n = int(input())
contador = 0
while n  != 0: 
    
    contador = contador + 1
    n = n // 10  
print(contador)
