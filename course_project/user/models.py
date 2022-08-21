from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255, unique=False)
    second_name = models.CharField(max_length=255, unique=False)
    tel = models.BigIntegerField(unique=True, null=False)

    def __str__(self):
        return self.first_name
