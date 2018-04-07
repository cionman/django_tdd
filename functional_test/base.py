import sys
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        """테스트 시작전 실행 되는 메소드 이며 최초 한번 만 실행"""
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def get_chrome_option(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--disable-default-apps')
        return chrome_options

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def setUp(self):
        """1. 테스트 시작 전 메소드,
           2. 테스트 시작전 메소드이며 테스트 함수가 실행될때마다 실행되기전에 실행"""

        self.browser = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver',
            chrome_options=self.get_chrome_option()
        )
        self.browser.implicitly_wait(3)  # 암묵적 대기 그 전에 로드되면 다음이 실행된다.

    def tearDown(self):
        """테스트 시작 후 메소드, 테스트에 에러가 발생해도 실행된다."""
        self.browser.quit()


