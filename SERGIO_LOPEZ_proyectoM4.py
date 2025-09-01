# pokedex.py
# Proyecto: Pokedex con Python y la API de pokeapi.co
# Autor: [Tu nombre]
# Este programa consulta la PokeAPI para mostrar datos de un Pokémon,
# valida errores, muestra resultados y guarda la información en un archivo JSON.

import requests # Librería para consumir APIs
import json     # Para guardar datos en archivos JSON
import os       # Para crear carpeta si no existe

# Crear carpeta 'pokedex' si no existe
if not os.path.exists("Pokedex"):
    os.makedirs("pokedex")

# Función principal
def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}" # Construir URL
    respuesta = requests.get(url) # Petición HTTP

    # Validar si la respuesta fue exitosa
    if respuesta.status_code == 200:
        datos = respuesta.json()

        # Extraer información importante
        info_pokemon = {
            "nombre": datos["name"],
            "peso": datos["weight"],
            "altura": datos["height"],
            "tipos": [t["type"]["name"] for t in datos["types"]],
            "habilidades": [h["ability"]["name"] for h in datos["abilities"]],
            "movimientos": [m["move"]["name"] for m in datos["moves"][:5]], # Solo 5 movimientos para no saturar
            "imagen": datos["sprites"]["front_default"]
        }

        # Mostrar información en consola
        print(f"Pokemon encontrado")
        print(f"Nombre: {info_pokemon['nombre']}")
        print(f"Peso: {info_pokemon['peso']}")
        print(f"Altura: {info_pokemon['altura']}")
        print(f"Tipos: {', '.join(info_pokemon['tipos'])}")
        print(f"Habilidades: {', '.join(info_pokemon['habilidades'])}")
        print(f"Movimientos: {', '.join(info_pokemon['movimientos'])}")
        print(f"Imagen: {info_pokemon['imagen']}")

        # Guardar en archivo JSON
        archivo = f"pokedex/{info_pokemon["nombre"]}.json"
        with open(archivo, "w") as f:
            json.dump(info_pokemon, f, indent=4) 

        print(f"\n Informacion guardada en: {archivo}")
    
    elif respuesta.status_code == 404:
        print("\n Error: Pokemon no encontrado.")
    else:
        print(f"\n Error inesperado: Codigo de estado: {respuesta.status_code}")

# ------------------- PROGRAMA PRINCIPAL -------------------
print("Bienvenido a tu Pokedex en Python!")
nombre = input("Ingresa el nombre de un Pokemon: ")
buscar_pokemon(nombre)
        

