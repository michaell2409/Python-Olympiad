# Repaso 3: Cuenta atrás en una línea
# Lee N e imprime de N a 1 en una sola línea y al final DESPEGUE.
# Ejemplo: 5 → 5 4 3 2 1 DESPEGUE | 1 → 1 DESPEGUE
# Idea: pego el espacio DETRÁS de cada número para que no sobre al principio.

n = int(input())
texto = ""
for i in range ((n), 0, -1):
	texto = texto  + str(i) + " "
print(texto + "DESPEGUE")
