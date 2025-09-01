Alumnos = []

while True:

    print("\n=== Menu Pricipal ===")
    print("1. Agregar un nuevo alumno")
    print("2. Ver los alumnos y las calificaciones")
    print("S. Salir")
    opcion = input("Seleccione una opcion: ").upper()

    if opcion == "1": 
        nombre = "" 
        while nombre.strip() == "":
            nombre = input("Ingrese el nombre del alumno: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")

        while True:
            try:
                cant = int(input("¿Cuantas calificaciones desea ingresar?: "))
                if cant > 0:
                    break
                else:
                    print("Debe ingresar un numero mayor a 0.")
            except ValueError:
                print("Error: debe ingresar un numero entero.")

        calificaciones = []

        for i in range(1, cant + 1):
            while True:
                try:
                    cal = float(input(f"Ingrese la calificacion {i}: "))
                    calificaciones.append(cal)
                    break
                except ValueError:
                    print("Error: la calificacion debe ser numerica.")
        
        Alumnos.append({"nombre": nombre, "calificaciones": calificaciones})
        print("Alumno agregado correctamente.")

    elif opcion == "2":
        if not Alumnos:
            print("No hay alumnos para mostrar.")
        else:
            for alumno in Alumnos:
                nombre = alumno["nombre"]
                calificaciones = alumno["calificaciones"]
                promedio = sum(calificaciones) / len(calificaciones)
                print(f"{nombre}: Promedio {promedio:.2f}")
    
    elif opcion == "S":
        confirmar = input("¿Estas seguro de que deseas salir? (S/N): ").upper()
        if confirmar == "S":
            print("Cerrando Programa.")
            break
    
    else:
        print("Opcion no valida, intente de nuevo.")
