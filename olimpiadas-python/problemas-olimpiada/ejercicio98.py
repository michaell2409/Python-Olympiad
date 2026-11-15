# Ejercicio 98: Codificador (Olimpiada de Las Palmas 2023, ejercicio 3)
# Consonante → su posición en el alfabeto español × 3; vocal → su posición en "uoiea". Siempre 2 cifras.
# ERROR si hay algún carácter fuera del alfabeto.
# Ejemplo: olimpiada → 023603395103051205 | verano → 690457054202
# Tiempo: 46 minutos (mi mejor tiempo en un P3)

import string
entrada = input().split()
abecedario = string.ascii_lowercase
abecedario = abecedario[:14] + "ñ" + abecedario[14:]
vocales = "uoiea"
resultado = []
real = ""
if len(entrada) == 1 and all(p.lower() in abecedario for p in entrada[0]):
	for i in entrada[0].lower():
		if i.lower() == "a" or i.lower() == "u" or i.lower() == "o" or i.lower() == "i" or i.lower() == "e":
			fuakabron = (vocales.index(i.lower())) + 1
			resultado.append(fuakabron) 
		else:
			otrica = abecedario.index(i) + 1 
			otrica = otrica * 3 
			resultado.append(otrica)
	for i in resultado:
		i = str(i)
		if len(i) == 1:
			i = "0" + i
			real = real + i
		else:
			real = real + i 	  	 

	print(real)			

			
else:
	print("ERROR")
