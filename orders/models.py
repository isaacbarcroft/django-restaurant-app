from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=255, default="name")
    phone_number = models.CharField(max_length=255, default="number")
    item = models.CharField(max_length=255, default="item")
    total_price = models.CharField(max_length=255, default="price")

    def __str__(self):
        return self.name