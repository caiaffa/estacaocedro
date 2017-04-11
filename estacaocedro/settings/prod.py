from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'estacaocedro',
        'USER': 'root',
        'PASSWORD': 'i3l1a2b3c#',
        'HOST': ''
    }
}

INSTALLED_APPS += (
	#'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1')

ALLOWED_HOSTS = ('*')
