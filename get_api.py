import requests
import json
URL = 'http://api.citybik.es/v2/networks/bikesantiago'


# response = requests.get(URL)
# data = response.json()
# print(data)


def get_api_content(url):
    headers = {'Content-Type': 'application/json, charset=utf-8', 'Access-Control-Allow-Origin': '*'}
    content = None

    try:
        response = requests.get(url, headers=headers)
        content = response.json()
    except requests.exceptions.RequestException as e:
        print(e)

    return content


hola = get_api_content(URL)
json_pretty_format = json.dumps(hola, indent=4)
print(json_pretty_format)

print(json_pretty_format['network']['stations'][0]['name'])
