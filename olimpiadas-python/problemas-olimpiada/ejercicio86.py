# Ejercicio 86: Huella de carbono (Olimpiada de Las Palmas 2024, ejercicio 1)
# Calcula los kg de CO2 de un viaje: emisión del transporte × km × pasajeros
# (coche 0.12, tren 0.05, avión 0.25, barco 0.20).
# Aprendido: los decimales "raros" (0.1 + 0.2) se arreglan con round(), redondeando ANTES de mirar si es entero.
# Ejemplo: coche 100 2 → 24 | barco 67.5 233 → 3145.5
# Tiempo: 15 minutos (mi primer P1 en tiempo de concurso)

tranporte, co, per = input().split()
if tranporte == "coche":
	resultado = 0.12 * float(co) * float(per)
elif tranporte == "tren":
	resultado = 0.05 * float(co) * float(per)
elif tranporte == "avión":
	resultado = 0.25 * float(co) * float(per)
elif tranporte == "barco":
	resultado = 0.20 * float(co) * float(per)	
resultado = round(resultado, 10)
if resultado.is_integer():
	print(int(resultado))	
else:
	print(resultado)
