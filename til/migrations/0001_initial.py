# Generated by Django 2.0.4 on 2018-04-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Til',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50)),
                ('date', models.DateField()),
                ('contents', models.TextField()),
                ('idate', models.DateTimeField(auto_now_add=True)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'til',
                'ordering': ['-date', '-idate'],
            },
        ),
    ]
