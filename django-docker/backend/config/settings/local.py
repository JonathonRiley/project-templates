import os
from .base import *
from .env_loader import EnvLoader

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


ENV = EnvLoader("local.env")

DEBUG= ENV.get_env_variable("DEBUG")
SECRET_KEY = ENV.get_env_variable("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ENV.get_env_variable("DATABASE_NAME"),
        'USER': ENV.get_env_variable("DATABASE_USER"),
        'PASSWORD': ENV.get_env_variable("DATABASE_PASSWORD"),
        'HOST': ENV.get_env_variable("DATABASE_HOST"),
        'PORT': "5432",
    },
}
