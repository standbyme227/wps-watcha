from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())
set_config(secrets, module_name=__name__, start=True)

WSGI_APPLICATION = 'config.wsgi.local.application'

ALLOWED_HOSTS = [

]

INSTALLED_APPS += [
    'django_extensions',
]
