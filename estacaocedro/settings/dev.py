from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'root',
        'USER': '',
        'PASSWORD': 'admin123',
        'HOST': ''
    }
}

INSTALLED_APPS += (
	#'debug_toolbar',
	'tinymce',
)

INTERNAL_IPS = ('127.0.0.1')