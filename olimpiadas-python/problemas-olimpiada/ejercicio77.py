# Ejercicio 77: Matriz Espiral (Olimpiada de Las Palmas 2025, ejercicio 3)
# Rellena una matriz n×n en espiral (de fuera a dentro, sentido horario) repitiendo la palabra.
# ERROR si n no está entre 1 y 20 o si la palabra tiene algo que no sean letras.
# Me atasqué y lo partí en trozos: ejercicios 78, 79, 80 y 81. Luego volví y lo saqué.
# Ejemplo: 4 bDujjFlavUsntYAya... → b D u j / n t Y j / s y A F / U v a l
# Tiempo: 2 horas y 54 minutos (repartido entre dos días, con los ejercicios 78-81 de por medio)

import string
uwu = input().split() 
if  len(uwu) == 2: 
	T = uwu[0]
	palabra = uwu[1]


	a = 0  

	contador = 0

	if len(palabra[0]) != " " and len(palabra[-1]) != " " and "  " not in palabra and   T.isdigit() and 1 <= int(T) <= 20 and  all(k in string.ascii_letters  for k in palabra ) :
		n = int(T)
		matriz  = [["."for i in range(n)] for q in range(n)]
		while a < (n+1)//2:
			if n%2 != 0 and  a == n//2:
				matriz[a][a] = palabra[contador % len(palabra)]
			else:	
				for w in range(a, n-a):
					matriz[a][w] = palabra[contador % len(palabra)]
					contador = contador + 1 
					

				for r in range(a+1, n-a-1):
					matriz[r][n-a-1] = palabra[contador%len(palabra)]
					contador = contador + 1
					

				for e in range(n-a-1, a-1, -1):
					matriz[n-a-1][e] = palabra[contador % len(palabra)]
					contador = contador + 1 

				for t in range(n-a-1-1, a, -1 ):
					matriz[t][a] = palabra[contador%len(palabra)]
					contador = contador + 1

			a = a + 1

			
			
		
		for linea in matriz:
			print(*linea)
	else:
		print("ERROR")
else:
	print("ERROR")		
