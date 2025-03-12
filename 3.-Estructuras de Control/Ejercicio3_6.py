uno = input("Dame un número: ")
dos = input("Dame otro número: ")
tres = input("Dame otro número: ")
cuatro = input("Dame otro número: ")
cinco = input("Dame el último número: ")

if uno >= dos:
    if uno >= tres:
        if uno >= cuatro:
            if uno >= cinco:
                frase = f"El número {uno} es el mayor"
                print(frase)
            else:
                frase = f"El número {cinco} es el mayor"
                print(frase)
        else:
                frase = f"El número {cuatro} es el mayor"
                print(frase)
    else:
        if tres >= cuatro:
            if tres >= cinco:
                frase = f"El número {tres} es el mayor"
                print(frase)
            else:
                frase = f"El número {cinco} es el mayor"
                print(frase)
else:
    if dos >= tres:
        if dos >= cuatro:
            if dos >= cinco:
                frase = f"El número {dos} es el mayor"
                print(frase)
            else:
                frase = f"El número {cinco} es el mayor"
                print(frase)
        else:
                frase = f"El número {cuatro} es el mayor"
                print(frase)
    else:
        if tres >= cuatro:
            if tres >= cinco:
                frase = f"El número {tres} es el mayor"
                print(frase)
            else:
                frase = f"El número {cinco} es el mayor"
                print(frase)
