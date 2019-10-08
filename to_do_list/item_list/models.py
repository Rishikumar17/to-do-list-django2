from django.db import models


# Create your models here.
class ItemList(models.Model):
    activity = models.CharField(max_length=100)

