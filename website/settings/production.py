import os
from website.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

env = os.environ.copy()

DB_NAME = env['DB_NAME']
DB_USER = env['DB_USER']
DB_PASS = env['DB_PASS']
DB_HOST = env['DB_HOST']

SECRET_KEY = env['SECRET_KEY']

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