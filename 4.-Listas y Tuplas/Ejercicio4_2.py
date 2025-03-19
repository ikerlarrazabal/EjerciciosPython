# Solicitar 5 números al usuario para la primera lista
lista1 = []
print("Introduce 5 números para la primera lista:")
for _ in range(5):
    num = int(input("Número: "))
    lista1.append(num)

# Solicitar 5 números al usuario para la segunda lista
lista2 = []
print("Introduce 5 números para la segunda lista:")
for _ in range(5):
    num = int(input("Número: "))
    lista2.append(num)

# Encontrar los números en común
comunes = list(set(lista1) & set(lista2))

# Mostrar los números en común
print("Números en común entre ambas listas:", comunes)
