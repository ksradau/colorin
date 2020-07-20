# Generated by Django 3.0.5 on 2020-04-19 08:31

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EducationPage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("h1", models.TextField(blank=True, null=True)),
                ("university", models.TextField(blank=True, null=True)),
                ("text", models.IntegerField(blank=True, null=True)),
            ],
            options={"verbose_name_plural": "Education Page",},
        ),
    ]
