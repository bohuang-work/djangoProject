import uuid

from django.db import models

from userAPI.models.user import UserDB


class ComputerDB(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    brand = models.CharField(max_length=64)
    user = models.ForeignKey(UserDB, on_delete=models.CASCADE, related_name="computers")

    def __str__(self):
        return self.brand
