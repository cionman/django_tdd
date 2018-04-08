# 실서버 설정
from conf.util import get_server_info_value
from .base import *

SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [
            "django-tdd.suwoni-codelab.com",
            ]

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']["default"]
}
