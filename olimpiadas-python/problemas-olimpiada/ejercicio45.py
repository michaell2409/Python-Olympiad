# Ejercicio 45: Números romanos, parte B: decimal → romano (Olimpiada de Tenerife 2026, ejercicio 4)
# Lee un número del 1 al 3999 y lo escribe en romano.
# Ejemplo: 58 → LVIII | 27 → XXVII | 1994 → MCMXCIV
# Idea: recorro la tabla de mayor a menor y, mientras el número quepa, resto el valor y apunto el símbolo.
# La tabla incluye las 6 parejas de resta (CM, CD, XC, XL, IX, IV); sin ellas el 4 saldría IIII.

valores  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

numero = int(input())
resultado = ""

for i in range(len(valores)):
    while numero >= valores[i]:
        numero = numero - valores[i]
        resultado = resultado + simbolos[i]

print(resultado)
