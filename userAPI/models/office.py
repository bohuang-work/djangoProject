import uuid

from django.db import models

from userAPI.models.user import UserDB


class OfficeDB(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=64)
    num_tables = models.IntegerField()
    user = models.ManyToManyField(UserDB, related_name="office")

    def __str__(self):
        return self.name
