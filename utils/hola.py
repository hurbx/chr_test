import requests
import json
import pandas as pd
from sqlalchemy import create_engine

database_name = 'db_chr2',
username = 'postgres',
password = 'postgres',
host = 'database-1.cglndfef2yaq.us-west-1.rds.amazonaws.com'

engine = create_engine('postgresql://postgres:postgres@database-1.cglndfef2yaq.us-west-1.rds.amazonaws.com/db_chr2')
URL = 'http://api.citybik.es/v2/networks/bikesantiago'


def get_api_data(url):
    try:
        data = requests.get(url)
        content = json.loads(data.content)

        return content

    except requests.exceptions.RequestException as e:
        print(e)




