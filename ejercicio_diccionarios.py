# emoji_diccionario = { "feliz": "😊", "amo": "😍", "risa": "🤣", "sonrisa": "😁", "llorar": "😭", "beso": "😘",
#     "aplauso": "👏", "reir": "😆", "fuego": "🔥", "roto": "💔", "pensando": "🤔",
#     "maravillado": "🤩", "aburrido": "😒", "guiño": "😉", "ok": "👌", "abrazo": "🤗",
#     "cool": "😎", "enojado": "😡", "python": "🐍"}

# frase = input('Escribe una frase: ')
# frase = frase.lower()
# palabras = frase.split()

# respuesta = " "

# for palabra in palabras:
#     if palabra in emoji_diccionario:
#         respuesta = respuesta + emoji_diccionario[palabra] + " "
#     else:
#         respuesta = respuesta + palabra + " "

# print(respuesta)


#####  Diccionario en otro idioma #####

colores_ingles = {
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue",
    "violeta": "violet"
}

colores_frances = {
    "rojo": "rouge",
    "naranja": "orange",
    "amarillo": "jaune",
    "verde": "vert",
    "azul": "bleu",
    "violeta": "violet"
}

print("Idiomas disponibles para traducir: Ingles - Frances")
idioma = input("¿A que idioma desea traducir? (ingles/frances):  ").lower()

if idioma not in["ingles", "frances"]:
    print("Idioma no valido solo puede elegir 'ingles' o 'frances'.")
else:
    frase = input("Escribe una frase con algun color: ").lower()
    palabras = frase.split()
    traduccion = ""

    for palabra in palabras:
        if idioma == "ingles" and palabra in colores_ingles:
            traduccion += colores_ingles[palabra] + " "
        elif idioma == "frances" and palabra in colores_frances:
            traduccion += colores_frances[palabra] + " "
        else:
            traduccion += palabra + " "
        
    print("Traduccion:", traduccion)