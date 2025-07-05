lista = []

while True:
    opcion = input('Agregue alumno (1) o Terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        
        calificaciones = []
        for i in range(3):
            agregar = input(f'¿Deseas agregar la calificación #{i+1}? (y/n): ')
            if agregar.lower() == 'y':
                nota = float(input(f'Ingrese la calificacion #{i+1} para {nombre}: '))
                calificaciones.append(nota)
            else:
                break

        if len(calificaciones) == 0:
            print("Debes ingresar al menos una calificacion.")
            continue

        alumno = [nombre] + calificaciones
        lista.append(alumno)

    elif opcion == '2':
        print(f'\nEl programa ha terminado con {len(lista)} alumno(s).\n')
        break
    else :
        print('Se ha ingresado una opcion invalida.')
        continue

print("Promedio de los alumnos:")
for alumno in lista:
    nombre = alumno[0]
    notas = alumno[1:]
    promedio = sum(notas) / len(notas)
    print(f'{nombre}: Promedio = {promedio:.2f}')