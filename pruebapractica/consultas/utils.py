import requests

def obtener_jurisprudencias():
    url = 'https://www.buscadorambiental.cl/buscador/api/v2/jurisprudencia/'
    # Realiza la petición POST
    response = requests.post(url, json={"list": True})
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []