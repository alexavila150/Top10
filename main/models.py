from django.db import models

# Create your models here.
class Item(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    