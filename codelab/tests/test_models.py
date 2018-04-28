from django.test import TestCase

from codelab.constants import Constant
from codelab.models import Codelab, CodelabCategory
from codelab.tests.base import CodelabModelBaseTest


class CodelabModelTest(CodelabModelBaseTest):

    def test_codelab_saving_test(self):
        """ 일반적인 Codelab model 저장 테스트 """

        codelab = self.save_codelab()
        self.assertEqual(codelab.user_id, Constant.TEST_CODELAB_DATA_USER_ID)
        self.assertEqual(codelab.user_name, Constant.TEST_CODELAB_DATA_USER_NAME)
        self.assertEqual(codelab.user_email, Constant.TEST_CODELAB_DATA_USER_EMAIL)
        self.assertEqual(codelab.title, Constant.TEST_CODELAB_DATA_TITLE)
        self.assertEqual(codelab.image, Constant.TEST_CODELAB_DATA_IMAGE)
        self.assertEqual(codelab.desc, Constant.TEST_CODELAB_DATA_DESC)
        self.assertEqual(codelab.isview, Constant.TEST_CODELAB_DATA_ISVIEW)
        self.assertEqual(codelab.category.category_name, Constant.TEST_CODELAB_DATA_CATEGORY)
        self.assertEqual(codelab.favorite, 0)

    def test_codelab_get_absolute_url(self):
        """ Codelab model get_absolute_url test"""

        codelab = self.save_codelab()
        self.assertEqual(codelab.get_absolute_url(), '/codelab/{}/'.format(codelab.id))


class CodelabDetailModelTest(CodelabModelBaseTest):

    def test_codelab_detail_saving_test(self):
        """ 일반적인 CodelabDetail model 저장 테스트 """

        codelab_detail = self.save_codelab_detail()
        self.assertEqual(codelab_detail.user_id, Constant.TEST_CODELAB_DATA_USER_ID)
        self.assertEqual(codelab_detail.user_name,
                         Constant.TEST_CODELAB_DATA_USER_NAME)
        self.assertEqual(codelab_detail.user_email,
                         Constant.TEST_CODELAB_DATA_USER_EMAIL)
        self.assertEqual(codelab_detail.title, Constant.TEST_CODELAB_DETAIL_DATA_TITLE)
        self.assertEqual(codelab_detail.contents, Constant.TEST_CODELAB_DETAIL_DATA_CONTENTS)
        self.assertEqual(codelab_detail.contents_markdown, Constant.TEST_CODELAB_DETAIL_DATA_CONTENTS_MARKDOWN)

    def test_codelab_detail_get_absolute_url(self):
        """ CodelabDetail model get_absolute_url test"""

        codelab_detail = self.save_codelab_detail()
        self.assertEqual(codelab_detail.get_absolute_url(), '/codelab/{}/'.format(codelab_detail.slug))