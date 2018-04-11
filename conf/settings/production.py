# 실서버 설정
from conf.util import get_server_info_value
from .base import *

SETTING_PRD_DIC = get_server_info_value("production")
SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [
            "django-tdd.suwoni-codelab.com",
            ]

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']["default"]
}
