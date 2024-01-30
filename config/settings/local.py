from pathlib import Path
from config.settings.env_reader import env, csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", cast=csv())
DEBUG = env("DEBUG", cast=bool)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}