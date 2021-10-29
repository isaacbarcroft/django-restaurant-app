from django.db import models


# Create your models here.
class Menuitem(models.Model):
        title = models.CharField(max_length = 255, default='SOME STRING')
        category = models.CharField(max_length = 255, default='SOME STRING')
        image = models.ImageField(upload_to='media/', null=True)
        price = models.IntegerField(null=True)
        desc =models.TextField(default='descr')

        def __str__(self):
            return self.title
