# Generated by Django 4.1.5 on 2023-01-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0016_alter_artist_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='source',
            field=models.URLField(verbose_name='Source That The Artist Is Canadian'),
        ),
    ]
