from django.db import models

from conf.models import CommonInfo


class Til(CommonInfo):
    date = models.DateField()  # 표시날짜
    contents = models.TextField()

    class Meta:
        db_table = 'til'
        ordering = ['-date', '-idate']

    def __str__(self):
        return str(self.date)
