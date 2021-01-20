import os
from website.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['nefonfo.pythonanywhere.com', 'localhost']

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getDB_NAME = os.getenv('DB_USER')
DB_PASS = os.getDB_NAME = os.getenv('DB_PASS')
DB_HOST = os.getDB_NAME = os.getenv('DB_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
    }
}

try:
    from .local import *
except ImportError:
    pass