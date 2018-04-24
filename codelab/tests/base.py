import os

from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile
from codelab.constants import Constant
from conf.settings.base import BASE_DIR


class CodelabViewBaseTest(TestCase):

    def writer_login(self):
        self.client.post('/accounts/login/', Constant.CREDENTIALS,
                         follow=True)

    def not_writer_login(self):
        self.client.post('/accounts/login/', Constant.NOT_WRITER_CREDENTIALS,
                         follow=True)

    def insert_codelab(self, data):
        response = self.client.post('/codelab/new/', data=data)

    def login_and_insert_codelab_with_default_data(self, is_writer = True):
        if is_writer:
            self.writer_login()
        else:
            self.not_writer_login()

        with open(os.path.join(BASE_DIR, "assets/image/logo.png"),
                  mode='rb') as image:
            self.codelab_data["image"] = image
            self.insert_codelab(data=self.codelab_data)

    def insert_codelab_detail(self):
        response = self.client.post('/codelab/new/detail/',
                                    data=self.codelab_detail_data)

    @classmethod
    def setUpClass(cls):
        if User.objects.count() == 0:
            user = User.objects.create_user(**Constant.CREDENTIALS)
            Profile.objects.create(user=user, is_writer=True, is_admin=False)
            not_writer_user = User.objects.create_user(
                **Constant.NOT_WRITER_CREDENTIALS)
            Profile.objects.create(user=not_writer_user, is_writer=False,
                                   is_admin=False)
        super().setUpClass()

    def setUp(self):
        self.codelab_data = {
            "title": Constant.TEST_CODELAB_DATA_TITLE,
            "desc": Constant.TEST_CODELAB_DATA_DESC,
            "isview": False,
        }
        self.codelab_detail_data = {
            "codelab": 1,
            "title": Constant.TEST_CODELAB_DETAIL_DATA_TITLE,
            "contents": Constant.TEST_CODELAB_DETAIL_DATA_CONTENTS,
            "slug": Constant.TEST_CODELAB_DETAIL_DATA_SLUG,
        }
        super().setUp()
