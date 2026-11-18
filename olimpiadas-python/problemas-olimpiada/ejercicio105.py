# Ejercicio 105: Huella de carbono (Olimpiada Informática de Las Palmas 2024, P1) - repaso de memoria
# Calcula los kg de CO2 de un viaje según el transporte, los km y los pasajeros.
# Ejemplo: coche 100 2 → 24 | barco 67.5 233 → 3145.5
# Tiempo: 12 minutos (la primera vez fueron 15)

transporte, numero, personas = input().split()
if transporte == "coche":
	transporte = 0.12 
if transporte == "tren":
	transporte = 0.05 
if transporte == "avión":
	transporte = 0.25 
if transporte == "barco":
	transporte = 0.20
resultado = transporte * float(numero) * float(personas)
resultado = round(resultado, 10)
if resultado.is_integer():
	print(int(resultado)) 
else:
	print(round(resultado, 10)	)
