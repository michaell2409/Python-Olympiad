# Ejercicio 88: Permutaciones Generativas (Olimpiada de Las Palmas 2024, ejercicio 3)
# Comprueba si los n números son una permutación de 0..n-1 (sin repetidos) y si la lista
# B, con b[i] = (a[i] + i) % n, tampoco tiene repetidos (generativa).
# Aprendido: contar repetidos con un diccionario. (El ejemplo 2 del enunciado oficial parece una errata.)
# Ejemplo: 1 2 0 → ES UNA PERMUTACIÓN GENERATIVA | 0 0 1 → NO ES UNA PERMUTACIÓN
# Tiempo: unas 2 horas (la mayor parte entendiendo el enunciado)

entrada = input().split()
contador = 0
for i in entrada:
	contador = contador + 1
contadorg = 0
contadordepermutaciones = 0 
sillas = []
contadorrialgforlife = 0  
dicionariopartedos = {}
dicionario = {}
if len(entrada) > 0 and all(i.isdigit() for i in entrada) and all(int(i) <= contador-1 for i in entrada):
	
	for i in (entrada):
		if i in dicionario:
			dicionario[i] = dicionario[i] + 1
		else:
			dicionario[i] = 1 	

	for i in dicionario:
		if dicionario[i] >= 2:
			print("NO ES UNA PERMUTACIÓN")
			contadordepermutaciones = contadordepermutaciones + 1 
			exit()
	if contadordepermutaciones == 0:
		for i in range(contador):
			sillas.append((int(entrada[i]) + i) % contador )
	for i in sillas:
		if i in dicionariopartedos:
			dicionariopartedos[i] = dicionariopartedos[i] + 1
		else:
			dicionariopartedos[i] = 1 
	for i in dicionariopartedos:
		if dicionariopartedos[i] >=	2:
			contadorrialgforlife = contadorrialgforlife + 1 
	if contadorrialgforlife > 0:		
		print("NO ES UNA PERMUTACIÓN GENERATIVA")
	else:
		print("ES UNA PERMUTACIÓN GENERATIVA")	 		  
	
				
			

else:
	print("ERROR")
