# Diccionario de usuarios con credenciales
usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

# Solicitar credenciales al usuario
usuario = input("Introduce tu usuario: ")
password = input("Introduce tu contraseña: ")

# Verificar credenciales
def login(usuario, password):
    if usuario in usuarios and usuarios[usuario]["password"] == password:
        print(f"Bienvenido {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}!")
    else:
        print("Usuario o contraseña incorrectos.")

# Ejecutar login
login(usuario, password)