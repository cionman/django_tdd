# 개발 설정
import os

from conf.util import get_server_info_value
from .base import *

SECRET_KEY = SETTING_DEV_DIC["SECRET_KEY"]
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    'default': SETTING_DEV_DIC['DATABASES']["default"]
}

