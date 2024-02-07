import uuid

from django.db import models


class UserDB(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    title = models.CharField(max_length=128)
    join_date = models.DateField(auto_now_add=True)
    active = models.BooleanField()

    def __str__(self):
        return self.name
