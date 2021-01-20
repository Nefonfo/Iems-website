import os
from .base import *

DEBUG = False

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = ['nefonfo.pythonanywhere.com', 'localhost']

DB_NAME = "nefonfo$website"
DB_USER = "nefonfo"
DB_PASS = "Kirisaki5501"
DB_HOST = "nefonfo.mysql.pythonanywhere-services.com"

SECRET_KEY = "8uf_))y&38+xn5%5*gdp51f++2+l71n2^*0elr0g9+lj4hu%"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
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