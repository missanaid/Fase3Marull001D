# Generated by Django 3.1.2 on 2020-11-24 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0021_auto_20201123_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='opening',
            field=models.URLField(blank=True, null=True),
        ),
    ]
