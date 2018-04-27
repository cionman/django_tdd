from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit

from conf.models import CommonInfo


class Codelab(CommonInfo):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='codelab/%Y/%m/%d',
                                help_text='대표이미지를 선택해주세요.')
    image_thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFit(400, 400)],  # 처리할 작업목록
        format='JPEG',
        options={'quality': 80},
    )
    desc = models.CharField(max_length=200)
    favorite = models.IntegerField(default=0)
    isview = models.BooleanField(default=True)
    category = models.ForeignKey('CodelabCategory', null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        db_table = 'codelab'
        ordering = ['-idate']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('codelab:codelab', args=[self.id])


class CodelabDetail(CommonInfo):
    codelab = models.ForeignKey('Codelab',
                                related_name='codelab_codelab_set',
                                on_delete=models.PROTECT,
                                )
    title = models.CharField(max_length=100)
    contents = models.TextField()
    contents_markdown = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        db_table = 'codelab_detail'
        ordering = ('-codelab',)

    def __str__(self):
        return '{} : {}'.format(self.id,
                                self.contents)

    def get_absolute_url(self):
        return reverse('codelab:codelab_detail', args=[self.slug])


class CodelabCategory(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
