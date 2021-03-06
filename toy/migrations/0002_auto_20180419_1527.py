# Generated by Django 2.0.4 on 2018-04-19 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toy',
            options={'ordering': ['-idate']},
        ),
        migrations.AlterField(
            model_name='toy',
            name='tech_stack',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toy',
            name='toy_image',
            field=models.ImageField(null=True, upload_to='toy/%Y/%m/%d'),
        ),
    ]
