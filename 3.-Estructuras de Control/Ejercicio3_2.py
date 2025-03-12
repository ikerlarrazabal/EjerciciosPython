primero = int(input("Dame un número entero: "))
segundo = int(input("Dame otro número entero: "))

contador = primero
suma = 0
    
while (contador <= segundo):
    suma = suma + contador
    contador = contador + 1
print(suma)
