from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'estacaocedro',
        'USER': 'i3l',
        'PASSWORD': 'admin123',
        'HOST': ''
    }
}

INSTALLED_APPS += (
	#'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1')

ALLOWED_HOSTS = ('*')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'generic': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            '()': 'logging.Formatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'server_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/server.log',
        },
        'request_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/request.log',
        },
        'template_file': {
            'class': 'logging.FileHandler',
            'formatter': 'generic',
            'filename': BASE_DIR + '/log/template.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    	'django.server':{
    		'handlers': ['console', 'server_file'],
    		'level': 'ERROR',
    		'propagate': False,
    	},
    	'django.request':{
    		'handlers': ['console', 'request_file'],
    		'level': 'ERROR',
    		'propagate': False,
    	},
    	'django.template':{
    		'handlers': ['console', 'template_file'],
    		'level': 'ERROR',
    		'propagate': False,
    	}
    },
}