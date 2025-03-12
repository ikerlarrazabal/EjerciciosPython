primero = int(input("Dame un número entero: "))
segundo = int(input("Dame otro número entero: "))

contador = primero
suma_par = 0
suma_impar = 0
    
while (contador <= segundo):
    if contador % 2 == 0:
        suma_par = suma_par + contador
    else:
        suma_impar = suma_impar + contador
    contador = contador + 1

resultado = f"La suma de los valores pares es de: {suma_par} y la suma de los valores impares es de: {suma_impar}"
print(resultado)
