from django.db import models

# Create your models here.
class Order(models.Model):
    item = models.CharField(max_length=255)
    total_price = models.CharField(max_length=255)

    def __str__(self):
        return self.title