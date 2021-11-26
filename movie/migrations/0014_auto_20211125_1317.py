# Generated by Django 3.2.9 on 2021-11-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20211125_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='screen_shots',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='screen_shots'),
        ),
    ]
