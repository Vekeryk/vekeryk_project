from os import environ
from app import create_app

app = create_app(environ.get('CONFIG_TYPE'))
