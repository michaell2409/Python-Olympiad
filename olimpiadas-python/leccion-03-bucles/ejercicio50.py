# Ejercicio 50: La entrada del cine para muchos (repaso: sys.stdin)
# Para cada línea con una edad, imprime el precio de la entrada.
# Ejemplo: 8, 30, 65 → 5, 9, 6

import sys
for linea in sys.stdin:
    edad = int(linea.strip())

    if edad < 12:
        print(5)
    elif edad < 65:
        print(9)
    else:
        print(6)
