# Utilizar al menos 2 funciones
# Preguntar cuantos alumnos se registraran, en caso
# Preguntara el nombre y 2 calificaciones
# Mostrar el nombre en pantalla con inicial mayuscula y promedio


def captura_alumnos(numero = 3):
    '''
    Registra alumnos y dos calificaciones
    Recibe como parametro la cantidad de alumnos a registrar
    Si no se especifica el numero de alumnos, se registraran 3
    '''
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f"{i + 1}.- Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificacion de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificacion de {nombre}: "))
        lista_alumnos.append([nombre, calificacion1, calificacion2])
        promedio(nombre, calificacion1, calificacion2)
    print("Las calificaciones de los alumnos son:", lista_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    '''
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parametro el nombre y dos calificaciones del alumno
    '''
    promedio = (calificacion1 + calificacion2) / 2
    print(f"El promedio es {nombre} es: {promedio}")



numero_alumnos = input("¿Cuantos alumnos desea registrar? ")

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos = int(numero_alumnos)
else:
    captura_alumnos()