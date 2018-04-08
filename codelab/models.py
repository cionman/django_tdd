from django.db import models


class Codelab(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='codelab/%Y/%m/%d'
                              , help_text='대표이미지를 선택해주세요.')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    desc = models.CharField(max_length=200)
    favorite = models.IntegerField(default=0)
    isview = models.BooleanField(default=True)
    idate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'codelab'
        ordering = ['-idate']

    def __str__(self):
        return self.title


class CodelabDetail(models.Model):
    codelab = models.ForeignKey('Codelab',
                                related_name='codelab_codelab_set',
                                on_delete=models.PROTECT,
                                )
    title = models.CharField(max_length=100)
    contents = models.TextField()
    idate = models.DateTimeField(auto_now_add=True)
    mdate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'codelab_detail'
        ordering = ('-codelab',)

    def __str__(self):
        return '{} : {}'.format(self.id,
                                self.contents)
