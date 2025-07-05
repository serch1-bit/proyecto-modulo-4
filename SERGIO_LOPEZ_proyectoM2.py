##### Longitud de una frase #####

# Pedir una frase al usuario
palabra = input("Escribe una palabra: ")

# Calcula la longitud (número de letras) de la palabra ingresada
longitud = len(palabra)

# Evalúa si la longitud está entre 4 y 8 letras (inclusive)
if 4 <= longitud <= 8:
    print("La palabra es correcta.") # Si la condición se cumple, se informa que la palabra es válida
# Si la longitud es menor a 4 letras
elif longitud < 4:
    print(f"La palabra es corta, solo tiene {longitud} letras.")  # Muestra que es una palabra corta
# Si la longitud es mayor a 8 letras
else :
    longitud > 8
    print(f"La palabra es muy larga, tiene {longitud} letras.") # Informa que la palabra es muy larga


##### Encuentra el cuadrante #####

# Solicita al usuario que ingrese un valor numérico para la coordenada X
x = float(input("Ingrese el valor de x: "))

# Solicita al usuario que ingrese un valor numérico para la coordenada y
y = float(input("Ingrese el valor de y: "))

# Verifica si alguna de las coordenadas es cero (lo cual es inválido para este programa)
if x == 0 or y == 0:
    print("Error: Ningun valor debe ser 0") # Muestra un mensaje de error si alguna coordenada es 0
else :
    # Si X es positivo y Y es positivo, el punto está en el primer cuadrante
    if x > 0 and y > 0:
        print(" El punto se encuentra en el cuadrante I")
    # Si X es negativo y Y es positivo, el punto está en el segundo cuadrante
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    # Si X es negativo y Y es negativo, el punto está en el tercer cuadrante
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    # Si X es positivo y Y es negativo, el punto está en el cuarto cuadrante
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV")
