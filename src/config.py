# Configuración de la BD
import os #Se usa os para leer variables de entorno, por ejemplo en producción o en Docker. En este caso no se utiliza.

DB_USER = 'root'
DB_PASSWORD = 'tu_contraseña_del_servidor'
DB_HOST = 'localhost:3306'
DB_NAME = 'nombre_de_la_base_de_datos'

SQLALCHEMY_DATABASE_URI = (f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

class Config:
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False