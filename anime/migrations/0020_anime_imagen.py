# Generated by Django 3.1.2 on 2020-11-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0019_auto_20201031_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='anime/'),
        ),
    ]
