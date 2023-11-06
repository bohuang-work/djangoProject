# Generated by Django 4.2.7 on 2023-11-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("age", models.IntegerField()),
                ("title", models.CharField(max_length=128)),
                ("join_date", models.DateField()),
                ("active", models.BooleanField()),
            ],
        ),
    ]
