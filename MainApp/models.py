from django.db import models
from datetime import datetime    

# Create your models here.
class Candle(models.Model):
    # banknift_id = models.AutoField(primary_key=True)
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    date = models.CharField(null=True, max_length=20)
    volume = models.FloatField(null=True)
   
