# Generated by Django 4.2.7 on 2024-02-07 22:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("userAPI", "0002_jobdb"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComputerDB",
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
                ("brand", models.CharField(max_length=64)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="computers",
                        to="userAPI.userdb",
                    ),
                ),
            ],
        ),
    ]
