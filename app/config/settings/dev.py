from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS = [

]

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DeFaultFilesStorage'
