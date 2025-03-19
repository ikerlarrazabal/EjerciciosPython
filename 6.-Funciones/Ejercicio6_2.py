import random

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def adivinarNumero():
    numero_secreto = random.randint(1, 10)
    while True:
        intento = int(input("Adivina el número (1-10): "))
        if intento < numero_secreto:
            print("El número es más alto.")
        elif intento > numero_secreto:
            print("El número es más bajo.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break

# Ejemplo de uso
num = int(input("Introduce un número para verificar si es primo: "))
if esPrimo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")

adivinarNumero()
