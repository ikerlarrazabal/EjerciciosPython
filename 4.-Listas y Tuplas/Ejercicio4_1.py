# Definir la lista inicial
lista = [12, 23, 5, 29, 92, 64]
print("Lista inicial:", lista)

# 1. Elimina el último número y añádelo al principio
ultimo = lista.pop()
lista.insert(0, ultimo)
print("Después de mover el último al principio:", lista)

# 2. Mueve el segundo elemento a la última posición
segundo = lista.pop(1)
lista.append(segundo)
print("Después de mover el segundo al final:", lista)

# 3. Añade el número 14 al comienzo de la lista
lista.insert(0, 14)
print("Después de añadir 14 al inicio:", lista)

# 4. Suma todos los números de la lista y añade el resultado al final
suma = sum(lista)
lista.append(suma)
print("Después de añadir la suma de los elementos al final:", lista)

# 5. Fusiona la lista con [4, 11, 32]
lista.extend([4, 11, 32])
print("Después de fusionar con [4, 11, 32]:", lista)

# 6. Elimina todos los números impares de la lista
lista = [num for num in lista if num % 2 == 0]
print("Después de eliminar los impares:", lista)

# 7. Ordena la lista de forma ascendente
lista.sort()
print("Después de ordenar la lista:", lista)

# 8. Vacía la lista
lista.clear()
print("Lista vacía:", lista)
