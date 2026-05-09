from .common import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['salesgame-prod-0d931d83aaf5.herokuapp.com']




DATABASES = {
    'default': {
        **dj_database_url.config(),
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

REDIS_URL = os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379/1')
CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', 'localhost')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', 2525)

INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'silk']
MIDDLEWARE = [m for m in MIDDLEWARE if 'silk' not in m]