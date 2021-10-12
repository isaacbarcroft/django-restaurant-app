from django.db import models


# Create your models here.
class Menuitem(models.Model):
        title = models.CharField(max_length = 255, default='SOME STRING')
        category = models.CharField(max_length = 255, default='SOME STRING')
        price = models.CharField(max_length = 255, default='SOME STRING')
       

        def __str__(self):
            return self.title
