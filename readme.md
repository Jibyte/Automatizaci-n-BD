Automatización de Bases de Datos

Este proyecto fue desarrollado en Python para automatizar la creación de una base de datos MySQL. El código se conecta al servidor local, verifica y crea la base de datos si no existe, define la estructura de la tabla personas_jimmy y genera e inserta de forma masiva 100,000 registros sintéticos optimizados mediante lotes.

Herramientas utilizadas:

* Python 3.
* MySQL
* SQLAlchemy y PyMySQL
* Faker (locale es_CO)

Instrucciones de instalación y ejecución:

1. Clona este repositorio en tu equipo y entra a la carpeta del proyecto:
git clone https://github.com/Jibyte/Automatizaci-n-BD
cd "Automatización BD"

2. Crea y activa un entorno virtual para aislar las dependencias:
python -m venv venv
venv\Scripts\activate

3. Instala las librerías necesarias con el siguiente comando:
pip install -r requirements.txt

4. Configura tus credenciales locales:
Crea un archivo llamado .env en la carpeta principal del proyecto, copia las variables de .env.example y escribe los datos de tu conexión MySQL:

DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=0000
DB_NAME=taller_db

5. Ejecuta el script principal con el comando:
python main.py