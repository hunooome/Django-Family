from .base import *

DEBUG = False

ALLOWED_HOSTS = env.list('STAGING_ALLOWED_HOSTS', default=['your-staging-domain.com'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('STAGING_DB_NAME'),
        'USER': env('STAGING_DB_USER'),
        'PASSWORD': env('STAGING_DB_PASSWORD'),
        'HOST': env('STAGING_DB_HOST'),
        'PORT': env('STAGING_DB_PORT'),
    }
}
