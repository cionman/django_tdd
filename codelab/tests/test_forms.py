from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Profile
from codelab.constants import Constant
from codelab.forms import CodelabForm


class CodelabFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        if not User.objects.filter(username=Constant.CREDENTIALS["username"]).count():
            cls.user = User.objects.create_user(**Constant.CREDENTIALS)
            Profile.objects.create(user=cls.user, is_writer=True,
                                   is_admin=False)
        super().setUpClass()