from utils.hola import get_api_data
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from sqlalchemy import create_engine
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

"""metodo para salir del programa"""


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def data_view():
    print('Has elegido la opción 2')
    print(
        'para ver la informacion ingresada en la base de datos debe ingresar a la siguiente direccion:http://127.0.0.1:8000/db_data/\nhttp:\nLuego de haber'
        ' ejecutado el comando python manage.py runserver')


def table_data():
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php')
    driver.maximize_window()
    len_array = driver.find_elements(by=By.TAG_NAME, value='option')
    nombre_list, tipo_list, region_list, tipologia_list, titular_list, inversion_list, fecha_list, estado_list = [], [], [], [], [], [], [], []
    count = 1
    data = pd.DataFrame()
    engine = create_engine(
        )
    for i in range(len(len_array)):
        selection = driver.find_element("xpath", "//select[@name='pagina_offset']")
        drop = Select(selection)
        drop.select_by_visible_text(str(count))
        nombres = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[2]')
        tipo = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[3]')
        region = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[4]')
        tipologia = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[5]')
        titular = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[6]')
        inversion = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[7]')
        fecha = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[8]')
        estado = driver.find_elements(By.XPATH, '//table[@class="tabla_datos"][1]/tbody/tr/td[9]')
        for nombre in nombres:
            nombre_list.append(nombre.text)
        for tipo in tipo:
            tipo_list.append(tipo.text)
        for region in region:
            region_list.append(region.text)
        for tipologia in tipologia:
            tipologia_list.append(tipologia.text)
        for titular in titular:
            titular_list.append(titular.text)
        for inversion in inversion:
            inversion_list.append(inversion.text)
        for fecha in fecha:
            fecha_list.append(fecha.text)
        for estado in estado:
            estado_list.append(estado.text)

        data = pd.DataFrame({'name': nombre_list,
                             'type': tipo_list,
                             'region': region_list,
                             'typology': tipologia_list,
                             'titular': titular_list,
                             'inversion': inversion_list,
                             'date': fecha_list,
                             'state': estado_list,
                             })
        print('Enviando DataFrame  a la BD')
        json_data = data.to_json('json_files/data.json', orient='records', indent=4)

        count += 1
        time.sleep(1)

        data.to_sql('chr_models_tabledata', con=engine, if_exists='append', index=False)


def menu_principal():
    opciones = {
        '1': ('Extraccion de Datos de la API', data_extraction),
        '2': ('Ver Datos Insertados en la DB', data_view),
        '3': ('Recoleccion de Datos de la Tabla', table_data),
        '4': ('Salir', cancel_program)
    }

    generar_menu(opciones, '4')


def data_extraction():
    """metodo que conecta a la api y comienza la extraccion de datos"""

    print('Has elegido la opción 1')
    print('Comenzando la conexion con la API y la extraccion de datos....')
    url = 'http://api.citybik.es/v2/networks/bikesantiago'
    fetch_data = get_api_data(url)

    company = fetch_data['network']['name']
    country = fetch_data['network']['location']['country']
    latitude = fetch_data['network']['location']['latitude']
    longitude = fetch_data['network']['location']['longitude']
    engine = create_engine('postgresql://postgres:postgres@database-1.cglndfef2yaq.us-west-1.rds.amazonaws.com/db_chr2')

    engine.execute('INSERT INTO chr_models_company (name, country, latitude, longitude)'
                   'VALUES (%s, %s, %s, %s)', (company, country, latitude, longitude))

    slots_list, address_list, altitude_list, ebikes_list, has_ebikes_list, normal_bike_list, last_update_list, \
        payment_list, free_bike_list, id_bike_list, latitude_list, longitude_list, name_list, time_list, quantity_list, \
        post_code_list, pay_terminal_list, uid_list, renting_list, returning_list, slots2_list = [], [], [], [], [], [], [], \
        [], [], [], [], [], [], [], [], [], [], [], [], [], []

    """Extraccion de Datos"""

    for i in fetch_data['network']['stations']:
        has_ebikes = i['extra']['has_ebikes']
        has_ebikes_list.append(has_ebikes)

    holi = fetch_data['network']['stations']
    for i in holi:
        if 'post_code' in i['extra']:
            post_code_list.append(i['extra']['post_code'])
        else:
            post_code_list.append('no data')

    for i in fetch_data['network']['stations']:
        slots = i['extra']['slots']
        slots2_list.append(slots)
        renting = i['extra']['renting']
        renting_list.append(renting)
        returning = i['extra']['returning']
        returning_list.append(returning)
        uid = i['extra']['uid']
        uid_list.append(uid)
        payment_terminar = i['extra']['payment-terminal']
        pay_terminal_list.append(payment_terminar)
        slots = i['empty_slots']
        slots_list.append(slots)
        address = i['extra']['address']
        address_list.append(address)
        altitude = i['extra']['altitude']
        altitude_list.append(altitude)
        ebikes = i['extra']['ebikes']
        ebikes_list.append(ebikes)
        normal_bikes = i['extra']['normal_bikes']
        normal_bike_list.append(normal_bikes)
        last_update = i['extra']['last_updated']
        last_update_list.append(last_update)
        payment_methods = i['extra']['payment']
        payment_list.append(payment_methods)
        free_bikes = i['free_bikes']
        free_bike_list.append(free_bikes)
        id_bike = i['id']
        id_bike_list.append(id_bike)
        latitude = i['latitude']
        latitude_list.append(latitude)
        longitude = i['longitude']
        longitude_list.append(longitude)
        name = i['name']
        name_list.append(name)
        timestamp = i['timestamp']
        time_list.append(timestamp)

    """Creacion de Dataframe"""
    data2 = pd.DataFrame({'empty_slots': slots_list,
                          'address': address_list,
                          'altitude': altitude_list,
                          'ebikes': ebikes_list,
                          'has_ebikes': has_ebikes_list,
                          'normal_bikes': normal_bike_list,
                          'last_updated': last_update_list,
                          'payment': payment_list,

                          'quantity': free_bike_list,
                          'id_bike': id_bike_list,
                          'latitude': latitude_list,
                          'longitude': longitude_list,
                          'name': name_list,
                          'time_stamp': time_list,
                          'company_id': 1,
                          'post_code': post_code_list,
                          'exist': pay_terminal_list,
                          'uid': uid_list,
                          'renting': renting_list,
                          'returning': returning_list,
                          'slots': slots2_list
                          })
    print('creando dataframe....')
    print(data2)
    data2.to_sql('chr_models_stations', schema='public', con=engine, if_exists='append', index=False)


def cancel_program():
    print('Saliendo')
    exit()


if __name__ == '__main__':
    menu_principal()
