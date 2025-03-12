numero_uno = int(input("Dame un número:   "))
numero_dos = int(input("Dame un segundo número:   "))
frase = input("Escribe una frase:   ")
numero_tres = numero_uno+numero_dos
substring = frase[numero_uno:numero_tres]
print(substring)