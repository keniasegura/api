import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-super-secreta'

    # Conexión PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:samipro@40.233.21.255:5432/autopartes'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
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

    DEBUG = os.environ.get('FLASK_DEBUG', True)
    PORT = int(os.environ.get('PORT', 5000))