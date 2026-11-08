# Ejercicio 53: Votaciones (repaso: diccionarios)
# Lee los nombres votados e imprime el más votado y sus votos.
# Ejemplo: ana luis ana pedro ana luis → ana 3

votos = list(input().split()) 
dicicionario = {}
resultado = []
for i in votos:
    if i in dicicionario:
        dicicionario[i] = dicicionario[i] + 1
    else:
        dicicionario[i] = 1      
for o in dicicionario:
    resultado.append(dicicionario[o])
p = int(max(resultado))
for q in dicicionario:
    if p == dicicionario[q]:
        print(q, dicicionario[q])
