def obtener_letras_adyacentes(letra):
    # Verifica si es mayúscula o minúscula
    if letra.islower():
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    elif letra.isupper():
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        print("Eso no es una letra válida.")
        return

    if letra in alfabeto:
        indice = alfabeto.index(letra)
        anterior = alfabeto[indice - 1] if indice > 0 else 'No hay anterior'
        siguiente = alfabeto[indice + 1] if indice < len(alfabeto) - 1 else 'No hay siguiente'

        print(f"Letra anterior: {anterior}")
        print(f"Letra siguiente: {siguiente}")
    else:
        print("Eso no es una letra válida.")

while True:
    entrada = input("Ingresa una letra (o escribe 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break
    elif len(entrada) == 1 and entrada.isalpha():
        obtener_letras_adyacentes(entrada)
    else:
         print("Entrada no válida. Por favor, ingresa solo una letra.")
