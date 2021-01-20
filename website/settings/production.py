import os
from .base import *

DEBUG = False

env = os.environ.copy()

DB_NAME = env['DB_NAME']
DB_USER = env['DB_USER']
DB_PASS = env['DB_PASS']
DB_HOST = env['DB_HOST']

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