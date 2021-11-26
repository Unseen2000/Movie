# Generated by Django 3.2.9 on 2021-11-26 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_alter_movie_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielink',
            name='type',
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movielink',
            name='link',
            field=models.URLField(help_text='Download link'),
        ),
    ]