# Generated by Django 5.1 on 2024-08-22 08:18

import django_summernote.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_created_by_post_updated_by_alter_post_cover_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostAttachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Defaults to filename, if left blank",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to=django_summernote.utils.uploaded_filepath
                    ),
                ),
                ("uploaded", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
