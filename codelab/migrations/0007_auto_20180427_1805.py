# Generated by Django 2.0.4 on 2018-04-27 09:05

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('codelab', '0006_auto_20180427_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codelab',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(help_text='대표이미지를 선택해주세요.', upload_to='codelab/%Y/%m/%d'),
        ),
    ]
