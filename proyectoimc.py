# Pedir nombre
nombre = input("Ingresa tu nombre: ")
while not nombre.isalpha():
    print("Solo se permiten letras.")
    nombre = input("Ingresa tu nombre: ")

apellido_paterno = input("Ingresa tu apellido paterno: ")
while not apellido_paterno.isalpha():
    print("Solo se permiten letras.")
    apellido_paterno = input("Ingresa tu apellido paterno: ")

apellido_materno = input("Ingresa tu apellido materno: ")
while not apellido_materno.isalpha():
    print("Solo se permiten letras.")
    apellido_materno = input("Ingresa tu apellido materno: ")

# Pedir edad
edad = input("Ingresa tu edad: ")
while not edad.isdigit():
    edad = input("Ingresa solo números para la edad: ")
edad = int(edad)

# Pedir peso
peso = input("Ingresa tu peso en kg: ")
while not peso.replace(".", "", 1).isdigit():
    peso = input("Ingresa solo números para el peso: ")
peso = float(peso)

# Pedir estatura
estatura = input("Ingresa tu estatura en metros: ")
while not estatura.replace(".", "", 1).isdigit():
    estatura = input("Ingresa solo números para la estatura: ")
estatura = float(estatura)

# Calculo del IMC
imc = peso / (estatura * estatura)

# Mostrar datos del Usuario :)
print("\n--- Datos del Usuario ---")
print(f"Hola tu Nombre completo es: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Tienes: {edad} años")
print(f"Pesas: {peso} kg")
print(f"Mides: {estatura} m")
print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

