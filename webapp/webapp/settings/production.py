from .base import *

DEBUG = False

ALLOWED_HOSTS = ['example.com']

STATIC_URL = 'https://static.example.com/'
STATIC_ROOT = os.path.join(BASE_DIR, 'tmp', 'static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
