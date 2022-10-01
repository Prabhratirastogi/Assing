from django.db import models
from datetime import datetime    

# Create your models here.
class Candle(models.Model):
    # banknift_id = models.AutoField(primary_key=True)
    open = models.FloatField(unique=True, null=True)
    high = models.FloatField(unique=True, null=True)
    low = models.FloatField(unique=True, null=True)
    close = models.FloatField(unique=True, null=True)
    date = models.DateTimeField(unique=True, null=True)
    volume = models.FloatField(unique=True, null=True)
   