# Generated by Django 2.0.4 on 2018-04-15 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codelab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodelabCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='codelab',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codelab.CodelabCategory'),
        ),
    ]
