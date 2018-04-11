# 개발 설정
import os

from conf.util import get_server_info_value
from .base import *

# dev SECRET_KEY 노출되어도 무방, 실서버와는 다름
SECRET_KEY = "buq*!eias((btkx11b689964cs7-at1gw%k^!oypi^1357f6@"
DEBUG = True

INSTALLED_APPS += [
    # addon
    'django_extensions',
    'debug_toolbar',
]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
