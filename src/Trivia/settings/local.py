from .base import *

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'Trivia',
        'USER': 'postgres',
        'PASSWORD': 'facundo7' ,
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

