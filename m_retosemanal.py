# m_retosemanal.py

# Función para crear una sola lista
def crear_lista():
    longitud = int(input("Ingrese la longitud de su lista: "))
    lista = []
    for i in range(longitud):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        lista.append(elemento)
    return lista


# Función para crear varias listas
def crear_varias_listas():
    num_listas = int(input("¿Cuántas listas desea crear? "))
    lista_de_listas = []
    for i in range(num_listas):
        print(f"\nCreando lista número {i+1}")
        nueva_lista = crear_lista()
        lista_de_listas.append(nueva_lista)
    return lista_de_listas


# Función para eliminar elementos repetidos en listas posteriores
def eliminar_valores_repetidos(lista_de_listas):
    for i in range(len(lista_de_listas) - 1):
        for j in range(i + 1, len(lista_de_listas)):
            lista_de_listas[i] = [
                elem for elem in lista_de_listas[i] if elem not in lista_de_listas[j]
            ]
    return lista_de_listas
