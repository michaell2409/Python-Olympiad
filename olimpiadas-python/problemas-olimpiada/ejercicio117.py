# Ejercicio 117: Codificador (Olimpiada Informática de Las Palmas 2023, P3) - repaso de memoria
# Codifica una palabra: cada consonante es su posición en el alfabeto español por 3 y cada vocal su posición
# en "uoiea", siempre con dos dígitos. Si hay algún carácter fuera del alfabeto, ERROR.
# Ejemplo: verano → 690457054202 | cha,cha,cha → ERROR
# Tiempo: 17 minutos (la primera vez fueron 46)

palabra = input()
abecedario = "abcdefghijklmnñopqrstuvwxyz"
vocales = "uoiea"
palabra = palabra.lower()
resultado = [] 
if  all(p in abecedario for p in palabra):
	for i in palabra:
		if i in vocales:
			resultado.append("0"+str(vocales.index(i)+1))
		else:
			casi = (abecedario.index(i)+1) * 3
			if casi > 9:
				resultado.append(casi)
			else:
				resultado.append("0" + str(casi))	 

	print(*resultado, sep="")		
else:
	print("ERROR")
