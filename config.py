import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Configuración principal de la aplicación Flask
class Config:
	# Clave secreta para seguridad de sesiones y tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-super-secreta'

    # Conexión PostgreSQL - Configuración de BDS
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:samipro@40.233.21.255:5432/autopartes'
	
# Desactivar seguimiento de modificaciones para mejor performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuracion optimizada para conexiones de BDS
	SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
        'connect_args': {
            'connect_timeout': 10,
            'keepalives': 1,
            'keepalives_idle': 30,
            'keepalives_interval': 10,
            'keepalives_count': 5
        }
    }

# Configuración de entorno y puerto
    DEBUG = os.environ.get('FLASK_DEBUG', True) # Modo desarrollo/producción
    PORT = int(os.environ.get('PORT', 5000)) # Puerto por defecto: 5000
