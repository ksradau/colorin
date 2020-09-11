# Generated by Django 3.1.1 on 2020-09-11 12:14

import apps.colorin.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorin', '0007_auto_20200829_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramphoto',
            name='photo',
            field=models.FileField(storage=apps.colorin.storage.PublicMediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='inst_profile_pic',
            field=models.FileField(storage=apps.colorin.storage.PublicMediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='uploadedphoto',
            name='photo',
            field=models.FileField(storage=apps.colorin.storage.PublicMediaStorage(), upload_to=''),
        ),
    ]
