# Generated by Django 5.0.3 on 2024-05-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_remove_movie_image_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]