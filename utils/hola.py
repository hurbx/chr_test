import requests
import json
import pandas as pd
from sqlalchemy import create_engine

database_name = 'db_chr2',
username = 'postgres',
password = 'postgres',
host = 'host'

engine = create_engine('postgresql://postgres:host/db_chr2')
URL = 'http://api.citybik.es/v2/networks/bikesantiago'


def get_api_data(url):
    try:
        data = requests.get(url)
        content = json.loads(data.content)

        return content

    except requests.exceptions.RequestException as e:
        print(e)




