# Generated by Django 3.0.5 on 2020-04-20 18:17

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0002_auto_20200419_1508"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("started_at", models.DateField(blank=True, null=True)),
                ("finished_at", models.DateField(blank=True, null=True)),
                ("summary", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
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
                ("name", models.TextField()),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Responsibility",
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
                ("summary", models.TextField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responsibilities",
                        to="resume.Project",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="technologies",
            field=models.ManyToManyField(
                related_name="project", to="resume.Technology"
            ),
        ),
    ]