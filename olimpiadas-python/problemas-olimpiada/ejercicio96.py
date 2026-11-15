# Ejercicio 96: Quinta sucesora (Olimpiada de Las Palmas 2023, ejercicio 2)
# Devuelve la letra 5 posiciones más adelante en el alfabeto español (con ñ), de forma circular y en minúscula.
# Idea mía: el abecedario escrito dos veces seguidas para no salirme de la lista al sumar 5.
# Ejemplo: h → m | X → c | { → ERROR
# Tiempo: 20 minutos

letra = input().split()
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
if len(letra) == 1  and letra[0].lower() in abecedario:

	resultado = abecedario.index(letra[0].lower())
	print(abecedario[resultado + 5 ])
else:
	print("ERROR")
