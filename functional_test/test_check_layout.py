## note :
# - functional 테스트 (기능 테스트) 외부 사용자 관점
# - FT는 사람이 이해할 수 있는 스토리를 가지고 있어야한다.
import sys
from unittest import skip

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class CheckLayoutTest(FunctionalTest):
    pass