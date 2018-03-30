from .base import *

DEBUG = False

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
]

INSTALLED_APPS += [
    'storages',
]

DEFAULT_FILE_STORAGE = 'config.storage.DeFaultFilesStorage'
