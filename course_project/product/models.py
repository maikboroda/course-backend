from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vendor_code = models.CharField(max_length=255, null=False, unique=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name
