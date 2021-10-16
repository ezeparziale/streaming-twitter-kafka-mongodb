import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'mongodb.env')
load_dotenv(dotenv_path)

dotenv_path = join(dirname(__file__), 'twitter_api.env')
load_dotenv(dotenv_path)

# API KEYS DE TWIITER
API_KEY = os.environ.get("TWITTER_API_KEY")
API_SECRET_KEY = os.environ.get("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# MONGODB
MONGODB_SERVER = 'localhost'
MONGODB_USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGODB_USER_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

# KAFKA
SERVER_KAFKA = 'localhost:9092'
TOPIC_NAME = 'twitter' # NOMBRE DEL TOPIC DE KAFKA

# CONFIGURACION PARA BUSQUEDA DE TUITS
TRACKS = ['#argentina','argentina','seleccion','messi','escaloneta','afa']
LOCATION = [-126.2,-56.0,22.3,58.9]
LANGUAGES = ['en','es']