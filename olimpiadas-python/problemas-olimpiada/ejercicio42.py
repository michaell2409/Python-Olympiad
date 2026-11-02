# Ejercicio 42: El CIF de la empresa (Olimpiada de Tenerife 2026, ejercicio 3)
# Calcula el carácter de control de un CIF (letra + 7 cifras) y lo añade al final.
# Si la letra es N, P, Q, R, S o W, el control es una letra (J=0, A=1 ... I=9).
# Ejemplo: A4233456 → A42334565 | Q1234567 → Q1234567D

import sys # para que el usuario pueda meter varios imputs  
def resultado(R): 								# creo la funcion que me va a dar el resultado 
	# primera parte impares y pares
	par = 0
	impar = 0  									# creo la variable y le pongo 0 para que tenga algo nose si habra que ponerle int   
	posicion = len(R) 							# la posicion de lo que me dan  
	for i in range(0,posicion): 				# recoro la lo que me dan sin la letra 
		if i % 2 != 0 : 			# [si la posicion es par] = en el enunciado dice si la posicion en la que esta el numero es par pero en python es alrevez por que empieza a contar desde el 0
			par = par + int(R[i]) 					# se suma todo y se guarda en la variable par
		else: 									# si la posicion es impar 
			impa = int(R[i]) * 2 					# se multiplica por dos 
			if impa < 10: 						# si es menor que 10 lo aagrego a lista de impares
				impar = impar + impa 
			else: 								# si no tengo que sumarle los dos digitos 
				impadividido = impa // 10 		# saco el primer digito
				restoimpa = impa % 10 			# saco el segundo digito
				ya = impadividido + restoimpa 	# resultado de la suma 
				impar = impar + ya  # resultado del impar
	# calculo control			
	suma = par + impar # sumo la parte impar y la apar 
	casi = suma % 10 # cojo la ultima cifra
	control = (10 - casi) % 10 # hago esta opercacion 
	uwu = str(control) # guardo el resultado 
	return uwu # cuando llame la funcion este va a ser el resultado 
for linea in sys.stdin: # para que el usuario pueda meter varias lineas esto son solo palabras nada de listas es decir tiene que meter una palabra a la vez  
	n = str(linea.strip()) # las separo
	m = n[1 : 9] # le quito la letra a lo que el usuario manda para poder trabajar con eso  
	rr = resultado(m) # llamo a la famosa funcion 
	if n[0] in "NPQRSW": # si la primera letra de la palabra es alguna de estas pasa lo siguiente !!!EN PYTHON SE CUENTA DESDE 0!!!   
		if int(rr) == 0:
			n = n + "J"
		elif int(rr) == 1:
			n = n + "A"
		elif int(rr) == 2:
			n = n + "B"
		elif int(rr) == 3: 
			n = n + "C"
		elif int(rr) == 4:
			n = n + "D"
		elif int(rr) == 5:
			n = n + "E"
		elif int(rr) == 6:
			n = n + "F"
		elif int(rr) == 7:
			n = n + "G"
		elif int(rr) == 8:
			n = n + "H"
		elif int(rr) == 9:
			n = n + "I" 	 				 	 			  
	else:
		n = n + rr # si no simplimente se le suma el ultimo numero al final y esto pasa por que en este momento el numero no es un numero si no que una letra por eso se puede hacer esta operacion
	print(str(n)) # mostramos lo que sea n para que n no salga en forma de lista si no en forma de palabra ponemos str 	
