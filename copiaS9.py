
ALFABETO_MIN = "abcdefghijklmnopqrstuvwxyz"
ALFABETO_MAY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Obtener_letras_adyacentes(letra):
    if letra.islower():
        alfabeto = ALFABETO_MIN
    elif letra.isupper():
        alfabeto = ALFABETO_MAY
    else:
        print("Eso no es una letra valida.")
        return
    
    if letra not in alfabeto:
        print("Eso no es una letra valida.")
        return
    
    i = alfabeto.index(letra)

    anterior = alfabeto[i - 1] if i > 0 else "No hay anterior"
    siguiente = alfabeto[i + 1] if i < len(alfabeto) - 1 else "No hay siguiente"

    print(f"Letra anterior: {anterior}")
    print(f"Letra siguiente: {siguiente}")

def bucle_principal():
    while True:
        entrada = input("Ingrese una letra o escriba (salir) para terminar: ")
        
        if entrada.lower() == "salir":
            print("programa terminado.")
            break

        if len(entrada) == 1 and entrada.isalpha():
            Obtener_letras_adyacentes(entrada)
        else:
            print("Entrada no valida. Por favor ingrese solo una letra.")

bucle_principal()