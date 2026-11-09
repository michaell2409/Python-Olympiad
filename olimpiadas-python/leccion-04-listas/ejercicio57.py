# Ejercicio 57: Descomprimir con números de una cifra (puente hacia el compresor)
# Lee un texto comprimido (letra, cifra, letra, cifra...) y lo descomprime.
# Ejemplo: a3b2c1 → aaabbc | a2b1a2 → aabaa | z9 → zzzzzzzzz
# Idea: recorro de 2 en 2; la letra está en i y su número en i+1. "a" * 3 da "aaa".

entrada = input()
q = len(entrada)
salida = "" 
for i in range(0, q, 2):
	w = entrada[i] * int(entrada[i+1])
	salida = salida + str(w)  
print(salida)
