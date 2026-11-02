# Ejercicio 36: Consonantes
# Función es_consonante(letra); imprime solo las consonantes de una palabra.
# Ejemplo: olimpiada → lmpd
# Idea: Una consonante es una letra que NO es vocal (not in).

def es_consonante(letra):
	return letra not in "aeiouAEIOU"
m = input()
otro = str()
for i in m:
	if es_consonante(i):
		otro = otro + i		
print(otro)
