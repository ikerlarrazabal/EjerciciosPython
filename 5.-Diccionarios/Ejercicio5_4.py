# Programa para registrar las notas de los estudiantes

# Diccionario para almacenar los datos de los estudiantes
estudiantes = {}

# Pedir al profesor los datos de hasta 10 estudiantes
num_estudiantes = min(int(input("¿Cuántos estudiantes vas a ingresar? (Máx. 10): ")), 10)

for i in range(1, num_estudiantes + 1):
    nombre = input(f"Introduce el nombre del estudiante {i}: ")
    nota = float(input(f"Introduce la nota de {nombre}: "))
    estudiantes[str(i)] = {"nombre": nombre, "nota": nota}

# Separar aprobados y suspendidos
aprobados = [estudiantes[key]["nombre"] for key in estudiantes if estudiantes[key]["nota"] >= 5.0]
suspendidos = [estudiantes[key]["nombre"] for key in estudiantes if estudiantes[key]["nota"] < 5.0]

# Calcular la nota media de la clase
nota_media = sum(estudiantes[key]["nota"] for key in estudiantes) / len(estudiantes)

# Mostrar resultados
print("\nLista de aprobados:", aprobados)
print("Lista de suspendidos:", suspendidos)
print("Nota media de la clase:", round(nota_media, 2))