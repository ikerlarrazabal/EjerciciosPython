
contador = 0

while (contador < 3):
    nombre = input("Introduce tu nombre:  ")
    password = input("Introduce tu contraseña:  ")
    if nombre == "root" and password == "toor":
        print("Bienvenué mai fren!")   
        break
    else: 
        contador = contador+1
        if contador < 3:
            print("Intenta de nuevo")
        else:  
            print("Has gastado todos los intentos")