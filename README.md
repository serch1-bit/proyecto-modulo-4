# 📚 Proyecto: Pokédex con Python

Este proyecto consiste en una Pokédex creada en Python que consume la API pública [PokeAPI](https://pokeapi.co/).  
Cuando ingresas el nombre de un Pokémon, el programa obtiene y muestra:

- Peso  
- Altura  
- Tipos  
- Habilidades  
- Movimientos (primeros 5)  
- Imagen frontal  

Además, guarda toda esta información en un archivo `.json` dentro de la carpeta **pokedex/**.

---

## 🚀 Requisitos

Antes de ejecutar, asegúrate de tener instalado Python 3 y la librería `requests`.  
Puedes instalarla con:

```bash
pip install requests
```

---

📦 Dependencias (bibliotecas necesarias)

Python: 3.9 o superior

Librerías de terceros:

  requests (para consumir la PokeAPI)

Módulos de la librería estándar (no se instalan): json, os

---

▶️ Cómo usarlo

1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:
"python pokedex.py"
4. Ingresa el nombre de un Pokémon (ejemplo: pikachu, bulbasaur, charmander).

---

📂 Archivos del repositorio
pokedex.py        # Código principal

README.md         # Explicación del proyecto

pokedex/          # Carpeta con archivos JSON generados

---

🖼 Ejemplo de salida

✅ Pokémon encontrado:

- Nombre: pikachu
- Peso: 60
- Altura: 4
- Tipos: electric
- Habilidades: static, lightning-rod
- Movimientos: mega-punch, pay-day, thunder-punch, slam, double-kick
- Imagen: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png

💾 Información guardada en: pokedex/pikachu.json

---

📘 Lo que aprendí

Cómo consumir una API con requests.

Cómo manejar status codes y validar errores.

Cómo guardar información en un archivo JSON.

Cómo organizar un proyecto en Python y subirlo a GitHub.

Y un poco más del mundo Pokémon ⚡.

