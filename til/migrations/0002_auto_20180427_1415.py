# Generated by Django 2.0.4 on 2018-04-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('til', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='til',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
