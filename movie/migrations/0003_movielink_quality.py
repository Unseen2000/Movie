# Generated by Django 3.2.9 on 2021-11-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20211125_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielink',
            name='quality',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
