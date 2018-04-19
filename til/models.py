from django.db import models


class Til(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    date = models.DateField()  # 표시날짜
    contents = models.TextField()
    idate = models.DateTimeField(auto_now_add=True)  # 등록일
    mdate = models.DateTimeField(auto_now=True)  # 수정일

    class Meta:
        db_table = 'til'
        ordering = ['-date', '-idate']

    def __str__(self):
        return str(self.date)
