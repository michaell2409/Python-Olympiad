# Ejercicio 66: Acceso Permitido (Olimpiada de Las Palmas 2026, ejercicio 1)
# Lee la hora actual y la hora límite (HH:MM) y dice si el acceso está PERMITIDO o DENEGADO,
# con la diferencia en minutos. Imprime ERROR si falta algún dato, el formato es incorrecto o está fuera de rango.
# Ejemplo: 09:45 10:00 → PERMITIDO / 15 | 12:30 12:15 → DENEGADO / 15 | 20:30 24:00 → ERROR
# Tiempo: unas 3 horas

def grande(m):
	if len(m) == 5:
		return(True)
lista = list(input().split())
if  len(lista) == 2:
	actual = lista[0]
	limite = lista[1] 
	if actual == "" or limite == "":
		print("ERROR")
	elif grande(actual) and grande(limite) and actual[2] == ":" and limite[2] == ":": 
		h1, m1 = actual.split(":")
		h2, m2 = limite.split(":")
		def numero(m):
			if m.isdigit():
				return(True)
		def tamaño(m):
			if len(m) == 2:
				return(True)
		def r24(m):
			if int(m) < 24:
				return(True)
		def r60(m):
			if int(m) < 60:
				return(True)
		def resta(a, b, c, d):
			e = int(c) - int(d) 
			r = int(a) - int(b)
			t = r * 60
			y = t + e 
			return(y)

		if tamaño(h1) and tamaño(h2) and tamaño(m1) and tamaño(m2) and numero(h1) and numero(h2) and numero(m1) and numero(m2)\
		 and r24(h1) and r24(h2) and r60(m1) and r60(m2):
			if int(h2) - int(h1) > 0:
				print("PERMITIDO")
				print(resta(h2, h1, m2, m1))
			elif int(h1) == int(h2):
				if int(m2) - int(m1) > 0:
					print("PERMITIDO")
					print(resta(h2, h1, m2, m1))
				elif int(m2) - int(m1) == 0:
					print("PERMITIDO")
					print("0") 	
				else:
					print("DENEGADO")
					print(resta(h1, h2, m1, m2))	
			else:
				print("DENEGADO")
				print(resta(h1, h2, m1, m2))			
		else:
			print("ERROR")	
	else:
		print("ERROR")
else:
	print("ERROR")
