# Generated by Django 3.2.9 on 2021-11-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movielink_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielink',
            name='quality',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
