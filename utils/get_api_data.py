import requests
import json

URL = 'http://api.citybik.es/v2/networks/bikesantiago'


def get_api_data(url):
    try:
        response = requests.get(url)
        content = json.loads(response.content)

        return content
    except requests.exceptions.RequestException as e:
        print(e)


hola = get_api_data(URL)
sala = hola['network']['stations']

print(hola)

for i in sala:
    pass #print(i['extra']['payment'])
  # print(i['extra']['altitude'])
  # print(i['extra']['address']) accedemos a la direccion dentro de stations y extra
  # print(i['empty_slots']) accedemos directamente
  # print(i['timestamp']) imprime la fecha y la hora dentro del diccionario en stations
  # print(i['name']) imprime el nombre de las estaciones dentro del diccionario en stations
