# Generated by Django 4.2.7 on 2024-02-07 21:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("userAPI", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobDB",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("active", models.BooleanField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job",
                        to="userAPI.userdb",
                    ),
                ),
            ],
        ),
    ]
