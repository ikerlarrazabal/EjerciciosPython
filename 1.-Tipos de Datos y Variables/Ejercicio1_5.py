frase = input("Introduce una frase:   ")
letra_reemplazo = input("Dame la letra a reemplazar:   ")
reemplazo = input("Dame el reemplazo:   ")

cant_veces = frase.count(letra_reemplazo)

print(cant_veces)


nueva_frase = frase.replace(letra_reemplazo, reemplazo)
print(nueva_frase)