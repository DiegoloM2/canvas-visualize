#Development settings

from .base import *

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SECRET_KEY = '5^32yv19c+-8cp84-*xwk*i8us1@)f!a3l$&+-0rnaw07+kg+5'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]