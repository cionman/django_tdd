# Generated by Django 2.0.4 on 2018-04-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codelab', '0002_auto_20180415_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codelab',
            name='slug',
        ),
        migrations.AddField(
            model_name='codelabdetail',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
