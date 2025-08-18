import random
import matplotlib.pyplot as plt

################################################
# Función que simula el recorrido de una canica
################################################
def simular_canicas(niveles=12):
    """
    Esta función simula el recorrido de una sola canica en una máquina de Galton.
    
    Parámetros:
        niveles (int): cantidad de niveles de obstáculos. 
                       Cada nivel tiene 2 posibles caminos: izquierda (0) o derecha (1).

    Retorna:
        contenedor (int): número de veces que la canica cayó hacia la derecha.
                          Ese valor representa el contenedor final donde terminó la canica.
    """
    contenedor = 0 # la canica empieza en el centro
    for _ in range(niveles):
        paso = random.choice([0, 1]) # 0 = izquierda, 1 = derecha
        contenedor += paso           # si cayó a la derecha, aumentamos el contador
    return contenedor

################################################
# Función que grafica los resultados en un hitograma
################################################
def graficar_histograma(resultados):
    """
    Esta función recibe la lista de contenedores finales de todas las canicas
    y genera un histograma que muestra cómo se distribuyeron.

    Parámetros:
        resultados (list): lista de enteros con el contenedor final de cada canica.
    """
    # Graficamos los resultados como histograma
    plt.hist(resultados, bins=range(14), edgecolor="black", color="blue")

    # Personalizamos el gráfico
    plt.title("Simulación de la Máquina de Galton (3000 canicas, 12 niveles)")
    plt.xlabel("Contenedores")
    plt.ylabel("Cantidad de canicas")
    
    # Mostramos el gráfico en pantalla
    plt.show()

################################################
# Programa principal
################################################
def main():
    # Definimos los parámetros de la simulación
    num_canicas = 3000 # cantidad de canicas que caerán
    niveles = 12       # cantidad de niveles de obstáculos
   
    # Generamos una lista con el resultado de cada canica
    resultados = [simular_canicas(niveles) for _ in range(num_canicas)]

    # Graficación de resultados
    graficar_histograma(resultados)


# Ejecución del programa
# Esta condición garantiza que el programa principal (main)
# solo se ejecute cuando corramos directamente este archivo
# y no si lo importamos en otro módulo.
if __name__ == "__main__":
    main()
    
    