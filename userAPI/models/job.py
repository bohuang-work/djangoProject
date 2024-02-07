import uuid

from django.db import models

from userAPI.models.user import UserDB


class JobDB(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.OneToOneField(UserDB, on_delete=models.CASCADE, related_name="job")
    name = models.CharField(max_length=64)
    active = models.BooleanField()

    def __str__(self):
        return self.name
