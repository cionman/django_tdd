import os

from PIL import Image
from django.test import TestCase
from django.urls import resolve, reverse

from codelab.views import *
from conf.settings.base import BASE_DIR


class CodelabViewResolveTest(TestCase):

    def test_get_codelab_list_view(self):
        found = resolve('/codelab/')
        self.assertEqual(found.func, get_codelab_list)

    def test_create_codelab_view(self):
        found = resolve('/codelab/new/')
        self.assertEqual(found.func, create_codelab)

    def test_create_codelab_detail_view(self):
        found = resolve('/codelab/new/detail/')
        self.assertEqual(found.func, create_codelab_detail)

    def test_update_codelab(self):
        found = resolve('/codelab/update/30/')
        self.assertEqual(found.func, update_codelab)

    def test_update_codelab_detail(self):
        found = resolve('/codelab/update/abc/')
        self.assertEqual(found.func, update_codelab_detail)

    def test_get_codelab(self):
        found = resolve('/codelab/3/')
        self.assertEqual(found.func, get_codelab)

    def test_get_codelab_detail(self):
        found = resolve('/codelab/abc/')
        self.assertEqual(found.func, get_codelab_detail)


class CodelabViewPostTest(TestCase):

    def setUp(self):
        self.image_file = Image.open(os.path.join(BASE_DIR, "assets/image/logo.png"))

    def test_create_codelab(self):
        response = self.client.post('/codelab/new/', data={
            "title": "first Test",
            "image": self.image_file,
            "desc": "desc",
            "isview": False,
        })

        print('response body :', response)

        new_codelab = Codelab.objects.first()
        self.assertEqual(new_codelab.title, 'first Test')
