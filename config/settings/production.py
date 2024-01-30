from datetime import timedelta
from config.settings.env_reader import env, csv

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG", cast=bool)
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}