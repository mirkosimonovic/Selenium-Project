import requests

def obtener_jurisprudencias():
    # URL de la API de jurisprudencias
    url = 'https://www.buscadorambiental.cl/buscador/api/v2/jurisprudencia/'

    # Realiza la petición POST a la API para obtener las jurisprudencias
    response = requests.post(url, json={"list": True})

    # Verifica si la respuesta es exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtiene los datos de la respuesta en formato JSON
        data = response.json()

        # Retorna los resultados de las jurisprudencias
        return data['results']
    else:
        # Si la respuesta no es exitosa, retorna una lista vacía
        return []
