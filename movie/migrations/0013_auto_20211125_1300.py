# Generated by Django 3.2.9 on 2021-11-25 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_auto_20211125_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='screen_shots',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screen_shots',
            field=models.ImageField(default=None, upload_to='screen_shots'),
            preserve_default=False,
        ),
    ]
