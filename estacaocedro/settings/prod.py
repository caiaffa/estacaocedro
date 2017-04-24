from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'estacaocedro',
        'USER': 'root',
        'PASSWORD': 'websitei3l@123',
        'HOST': ''
    }
}

INTERNAL_IPS = ('127.0.0.1')

ALLOWED_HOSTS = ('*')
