lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]

# Crear un diccionario para contar la frecuencia de cada número
frecuencia = {}
for num in lista:
    if num in frecuencia:
        frecuencia[num] += 1
    else:
        frecuencia[num] = 1

# Mostrar el diccionario con las frecuencias
print("Frecuencia de números en la lista:", frecuencia)

resultado = f"Frecuencia de númericos:  {frecuencia} "

print(resultado)