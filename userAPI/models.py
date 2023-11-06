from django.db import models

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    title = models.CharField(max_length=128)
    join_date = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.name
