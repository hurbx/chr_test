# chr_test

### Notas.

- la carpeta applications contiene la unica aplicacion de Django que generamos para este proyecto, los modelos,
las urls y las vistas 
- El directorio utils contiene archivos para la obtencion de la informacion de la API 
- el archivo Main contiene el programa principal el cual inicia la obtencion de los datos y enviar estos a los modelos
- Se una una instancia de AWS-RDS que contiene la base de Datos PostgresSQL

### Descripcion.

El siguiente proyecto es la realizacion de dos tareas presentadas
en el documento enviado por correo electronico 
las tareas son las siguientes:


### Tarea 1

Dada la siguiente API pública http://api.citybik.es/v2/networks/bikesantiago (Bike Santiago)
desarrolle los siguiente requerimientos:
- Crear una función que obtenga la información presentada en la API pública (librerías
a utilizar: requests, urllib3 o aiohttp).
- Crear un modelo para la información obtenida.
- Guardar en el modelo la información obtenida desde el API.
- Opciona l. Generar vista en el administrador para visualizar la información obtenida.
- Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

![img.png](img.png)


















### Tarea 2
Dada la siguiente url https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php (Servicio
de Evaluación Ambiental) desarrolle los siguiente requerimientos:
- Crear un script para obtener la información presentada en la tabla de la url
proporcionada (librerías a utilizar: BeautifulSoup o Selenium).
- El script deberá recorrer todas las páginas y obtener la información de las tablas.
- El script deberá crear un archivo .json con la información obtenida.
- Generar modelo para guardar la información obtenida.
- Opcional. Generar vista en el administrador para visualizar la información obtenida.
- Opcional. Generar una vista con la información en Bootstrap 5 u otro similar


### 