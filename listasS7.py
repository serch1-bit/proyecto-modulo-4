lista = []

alumnos = 0
while alumnos <= 5:
    opcion = input('Agregue alumno (1) o Terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        calificacion3 = int(input(f'Ingrese la tercera calificacion de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2, calificacion3]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else :
        print('Se ha ingresado una opcion invalida.')
        continue

print('La lista de alumnos es:')
print(lista)