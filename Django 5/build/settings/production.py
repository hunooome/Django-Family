from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list('PROD_ALLOWED_HOSTS', default=['your-production-domain.com'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('PROD_DB_NAME'),
        'USER': env('PROD_DB_USER'),
        'PASSWORD': env('PROD_DB_PASSWORD'),
        'HOST': env('PROD_DB_HOST'),
        'PORT': env('PROD_DB_PORT'),
    }
}
