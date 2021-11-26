# Generated by Django 3.2.9 on 2021-11-25 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_movie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreenShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='screen_shots')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='screen_shots',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.screenshot'),
        ),
    ]