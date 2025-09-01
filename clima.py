import requests

def obtener_clima(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    respuesta = requests.get(url, params=params)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        humedad = datos["main"]["humidity"]

        print(f"Temperatura: {temp}°C")
        print(f"Clima: {descripcion}")
        print(f"Humedad: {humedad}%")
    else:
        print("Error al obtener datos:", respuesta.status_code, respuesta.text)


# Ejemplo de uso
API_KEY = "9ebbc1845825812e356dbc6e77e1c493"
latitud = 40.712784
longitud = -74.005941

obtener_clima(latitud, longitud, API_KEY)   


