# Hacer que el sistema genere un número aleatorio entre 1 y 10. 
# Luego, hacer que el usuario adivine el número.
# La aplicación debe terminar cuando el usuario adivine.

import random
s = random.randint(1, 10)

while True:
    n = int(input("Adivina el número del sistema (1...10): "))
    if n == s:
        print("Adivinaste, crack !")
        break
    else:
        print("Número incorrecto")