# Repaso 5: ¿Es primo?
# Para cada línea con un número mayor que 1, imprime PRIMO o NO PRIMO.
# Ejemplo: 7 → PRIMO | 12 → NO PRIMO | 49 → NO PRIMO
# Idea: cuento los divisores entre 2 y N-1. Si no hay ninguno, es primo.
# Mejora pendiente: basta con buscar divisores hasta la raíz cuadrada de N.

import sys 
for linea in sys.stdin: 
	n = int(linea.strip())
	contador = 0
	for i in range (2,n):
		m = n % i 
		if m == 0: 
			contador = contador + 1 
	if contador == 0: 
		print("PRIMO")
	else:
		print("NO PRIMO")
