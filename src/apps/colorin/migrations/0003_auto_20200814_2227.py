# Generated by Django 3.0.8 on 2020-08-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorin', '0002_remove_instagramprofile_inst_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramprofile',
            name='inst_biography',
            field=models.TextField(blank=True, default='Without Bio', null=True),
        ),
    ]
