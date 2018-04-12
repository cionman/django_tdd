from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
