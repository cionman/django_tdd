from django.db import models


class CommonInfo(models.Model):
    """ 공통 모델 정보 """

    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    idate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True