personas = []

# Cargar contactos desde archivo
try:
    with open("agenda.txt", "r") as f:
        for linea in f:
            personas.append(linea.strip().split(","))
except FileNotFoundError:
    pass

while True:
    print("""
1. Agregar persona
2. Guardar en archivo
3. Mostrar contactos
4. Modificar contacto
5. Salir
""")
    op = input("Opción: ")

    if op == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        correo = input("Correo: ")
        tel = input("Teléfono: ")
        personas.append([nombre, apellido, edad, correo, tel])

    elif op == "2":
        with open("agenda.txt", "w") as f:
            for p in personas:
                f.write(",".join(p) + "\n")
        print("Guardado en agenda.txt")

    elif op == "3":
        for i, p in enumerate(personas, start=1):
            print(f"{i}. {p[0]} {p[1]} - Edad: {p[2]} - Correo: {p[3]} - Tel: {p[4]}")

    elif op == "4":
        for i, p in enumerate(personas, start=1):
            print(f"{i}. {p[0]} {p[1]} - {p[3]} - {p[4]}")
        num = int(input("Número de contacto a modificar: ")) - 1
        if 0 <= num < len(personas):
            print("1. Nombre\n2. Correo\n3. Teléfono")
            op2 = input("Opción: ")
            if op2 == "1":
                personas[num][0] = input("Nuevo nombre: ") or personas[num][0]
                personas[num][1] = input("Nuevo apellido: ") or personas[num][1]
            elif op2 == "2":
                personas[num][3] = input("Nuevo correo: ") or personas[num][3]
            elif op2 == "3":
                personas[num][4] = input("Nuevo teléfono: ") or personas[num][4]
            print("Contacto actualizado.")

    elif op == "5":
        break
    else:
        print("Opción inválida")

