import os
import time

from PIL import Image
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse, Resolver404

from accounts.models import Profile
from codelab.tests.base import CodelabViewBaseTest
from codelab.views import *
from conf.settings.base import BASE_DIR


class CodelabViewPostTest(CodelabViewBaseTest):
    """view post 동작 테스트"""

    def test_create_codelab(self):
        """코드랩 정상 작성"""

        self.login_and_insert_codelab_with_default_data()
        new_codelab = Codelab.objects.first()
        self.assertEqual(new_codelab.title, Constant.TEST_CODELAB_DATA_TITLE)

    def test_create_codelab_detail(self):
        """코드랩 상세 정상 작성"""

        self.login_and_insert_codelab_with_default_data()
        self.insert_codelab_detail()

        new_codelab_detail = CodelabDetail.objects.first()
        self.assertEqual(new_codelab_detail.title,
                         Constant.TEST_CODELAB_DETAIL_DATA_TITLE)

    def test_update_codelab(self):
        """codelab 수정 업데이트"""

        self.login_and_insert_codelab_with_default_data()
        with open(os.path.join(BASE_DIR, "assets/image/logo.png"),
                  mode='rb') as image:
            self.codelab_data["image"] = image
            self.codelab_data["title"] = Constant.TEST_UPDATE_CODELAB_DATA_TITLE
            self.client.post('/codelab/update/1/', data=self.codelab_data)
            self.assertEqual(Codelab.objects.first().title,
                             Constant.TEST_UPDATE_CODELAB_DATA_TITLE)

    def test_update_codelab_without_modify_image(self):
        """codelab 이미지 없이 수정 업데이트"""

        self.login_and_insert_codelab_with_default_data()
        del self.codelab_data["image"]
        self.codelab_data["title"] = Constant.TEST_UPDATE_CODELAB_DATA_TITLE
        self.client.post('/codelab/update/1/', data=self.codelab_data)
        self.assertEqual(Codelab.objects.first().title,
                         Constant.TEST_UPDATE_CODELAB_DATA_TITLE)


    def test_update_codelab_detail(self):
        """codelab detail  수정 업데이트"""
        self.login_and_insert_codelab_with_default_data()
        self.insert_codelab_detail()
        self.codelab_detail_data[
            "slug"] = Constant.TEST_UPDATE_CODELAB_DATA_SLUG
        self.client.post(
            '/codelab/update/{}/'.format(Constant.TEST_CODELAB_DETAIL_DATA_SLUG)
            , data=self.codelab_detail_data)

        self.assertEqual(CodelabDetail.objects.first().slug,
                         Constant.TEST_UPDATE_CODELAB_DATA_SLUG)

    def test_create_codelab_big_image(self):
        """ 2.5메가 이상 이미지 에러 메세지 노출 테스트"""

        with open(
                os.path.join(BASE_DIR, "assets/image/test/test-big-image.jpg"),
                mode='rb') as image:
            self.writer_login()
            self.codelab_data["image"] = image
            response = self.client.post('/codelab/new/', data=self.codelab_data)
            self.assertIn('<ul class="errorlist nonfield"><li>최대 파일사이즈는',
                          response.content.decode())

    def test_create_codelab_attach_no_img(self):
        """ 이미지가 아닌 파일 첨부시 """

        with open(
                os.path.join(BASE_DIR, "assets/image/test/test.txt"),
                mode='rb') as image:
            self.writer_login()
            self.codelab_data["image"] = image
            response = self.client.post('/codelab/new/', data=self.codelab_data)
            self.assertIn(
                '<ul class="errorlist"><li>올바른 이미지를 업로드하세요. 업로드하신 파일은 이미지 파일이 아니거나 파일이 깨져 있습니다.',
                response.content.decode())

    def test_codelab_empty_title(self):
        """title 빈 값시 저장 안됨 확인"""

        self.writer_login()
        with open(os.path.join(BASE_DIR, "assets/image/logo.png"),
                  mode='rb') as image:
            self.codelab_data["image"] = image
            self.codelab_data["title"] = ""
            self.insert_codelab(data=self.codelab_data)

        self.assertEqual(0, Codelab.objects.count())

    def test_codelab_empty_image(self):
        """Image 빈 값 전달 시 저장 안됨 확인"""

        self.writer_login()
        self.codelab_data["image"] = ""
        self.insert_codelab(data=self.codelab_data)
        self.assertEqual(0, Codelab.objects.count())

    def test_codelab_empty_desc(self):
        """desc 빈 값시 저장 안됨 확인"""

        self.writer_login()
        with open(os.path.join(BASE_DIR, "assets/image/logo.png"),
                  mode='rb') as image:
            self.codelab_data["image"] = image
            self.codelab_data["desc"] = ""
            self.insert_codelab(data=self.codelab_data)
        self.assertEqual(0, Codelab.objects.count())

    def test_codelab_empty_isview(self):
        """isview 빈 값시 저장됨을  확인"""

        self.writer_login()
        with open(os.path.join(BASE_DIR, "assets/image/logo.png"),
                  mode='rb') as image:
            self.codelab_data["image"] = image
            self.codelab_data["isview"] = ""
            self.insert_codelab(data=self.codelab_data)
        self.assertEqual(1, Codelab.objects.count())

    def test_codelab_detail_empty_codelab(self):
        """codelab detail 에서 codelab 빈 값시 저장 안됨을 확인"""

        self.codelab_detail_data["codelab"] = ""
        response = self.client.post('/codelab/new/detail/',
                                    data=self.codelab_detail_data)
        self.assertEqual(0, CodelabDetail.objects.count())

    def test_codelab_detail_empty_title(self):
        """codelab detail 에서 title 빈 값시 저장 안됨을 확인"""

        self.login_and_insert_codelab_with_default_data()
        self.codelab_detail_data["title"] = ""
        response = self.client.post('/codelab/new/detail/',
                                    data=self.codelab_detail_data)
        self.assertEqual(0, CodelabDetail.objects.count())

    def test_codelab_detail_empty_contents(self):
        """codelab detail 에서 contents 빈 값시 저장 안됨을 확인"""

        self.login_and_insert_codelab_with_default_data()
        self.codelab_detail_data["contents"] = ""
        response = self.client.post('/codelab/new/detail/'
                                    , data=self.codelab_detail_data)
        self.assertEqual(0, CodelabDetail.objects.count())

    def test_codelab_detail_empty_slug(self):
        """codelab detail 에서 slug 빈 값시 저장 안됨을 확인"""

        self.login_and_insert_codelab_with_default_data()
        self.codelab_detail_data["slug"] = ""
        response = self.client.post('/codelab/new/detail/',
                                    data=self.codelab_detail_data)
        self.assertEqual(0, CodelabDetail.objects.count())

    def test_not_writer_create_codelab(self):
        """권한 없는 사용자 codelab 작성이 안됨을 확인"""

        self.login_and_insert_codelab_with_default_data(is_writer=False)
        self.assertEqual(Codelab.objects.count(), 0)

    def test_not_writer_create_codelab_detail(self):
        """권한 없는 사용자 codelab detail 작성이 안됨을 확인"""

        self.login_and_insert_codelab_with_default_data(is_writer=False)
        self.insert_codelab_detail()
        self.assertEqual(CodelabDetail.objects.count(), 0)


class CodelabViewLoadTest(CodelabViewBaseTest):
    """기본 화면 로드 테스트, 로그인 하지 않았을 시 테스트"""

    def test_get_codelab_list(self):
        response = self.client.get('/codelab/')
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_LIST_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_codelab(self):
        self.login_and_insert_codelab_with_default_data()
        response = self.client.get('/codelab/1/')
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_codelab_detail(self):
        self.login_and_insert_codelab_with_default_data()
        self.insert_codelab_detail()
        response = self.client.get(
            '/codelab/{}/'.format(Constant.TEST_CODELAB_DETAIL_DATA_SLUG))
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_DETAIL_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_create_codelab(self):
        self.writer_login()
        response = self.client.get('/codelab/new/')
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_CREATE_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_create_codelab_detail(self):
        self.writer_login()
        response = self.client.get('/codelab/new/detail/')
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_DETAIL_CREATE_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_update_codelab(self):
        self.login_and_insert_codelab_with_default_data()
        response = self.client.get('/codelab/update/1/')
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_UPDATE_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_get_update_codelab_detail(self):
        self.login_and_insert_codelab_with_default_data()
        self.insert_codelab_detail()
        response = self.client.get('/codelab/update/{}/'.format(
            Constant.TEST_CODELAB_DETAIL_DATA_SLUG))
        title_outerhtml = "<title>{}</title>".format(
            Constant.CODELAB_UPDATE_DETAIL_PAGE_TITLE)
        self.assertIn(title_outerhtml, response.content.decode())

    def test_not_login_create_codelab(self):
        response = self.client.get('/codelab/new/')
        self.assertEqual("/accounts/login/?next=/codelab/new/", response.url)

    def test_not_login_create_codelab_detail(self):
        response = self.client.get('/codelab/new/detail/')
        self.assertEqual("/accounts/login/?next=/codelab/new/detail/",
                         response.url)

    def test_not_login_update_codelab(self):
        self.login_and_insert_codelab_with_default_data()
        self.client.post('/accounts/logout/')
        response = self.client.get('/codelab/update/1/')
        self.assertEqual("/accounts/login/?next=/codelab/update/1/", response.url)

    def test_not_login_update_codelab_detail(self):
        self.login_and_insert_codelab_with_default_data()
        self.insert_codelab_detail()
        self.client.post('/accounts/logout/')
        response = self.client.get('/codelab/update/{}/'.format(Constant.TEST_CODELAB_DETAIL_DATA_SLUG))
        self.assertEqual("/accounts/login/?next=/codelab/update/{}/".format(Constant.TEST_CODELAB_DETAIL_DATA_SLUG)
                         , response.url)


    def test_not_writer_create_codelab(self):
        self.not_writer_login()
        response = self.client.get('/codelab/new/')
        self.assertEqual("/accounts/login/?next=/codelab/new/", response.url)

    def test_not_writer_create_codelab_detail(self):
        self.not_writer_login()
        response = self.client.get('/codelab/new/detail/')
        self.assertEqual("/accounts/login/?next=/codelab/new/detail/",
                         response.url)


class CodelabViewCheckFormTest(CodelabViewBaseTest):
    """get 화면에서 정상적인 form을 확인하는지 테스트"""

    def check_form(self, url, form):
        self.writer_login()
        response = self.client.get(url)
        self.assertIsInstance(response.context['form'], form)

    def test_codelab_new_uses_codelab_form(self):
        self.check_form('/codelab/new/', CodelabForm)


class CodelabViewResolveTest(TestCase):
    """Codelab url과 함수 매핑 테스트"""

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


class CodelabViewResolveFailTest(TestCase):
    """Codelab url과 함수 매핑 실패해야하는 테스트"""

    def test_fail_case_1(self):
        with self.assertRaises(Resolver404):
            found = resolve('codelab/new/3')

    def test_fail_case_2(self):
        with self.assertRaises(Resolver404):
            found = resolve('codelab/new/detail/3')

    def test_fail_case_3(self):
        with self.assertRaises(Resolver404):
            found = resolve('codelab/update/30/abc')

    def test_fail_case_4(self):
        with self.assertRaises(Resolver404):
            found = resolve('codelab/update/abc/3')
