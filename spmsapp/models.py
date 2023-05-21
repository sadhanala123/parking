from django.db import models
from datetime import datetime

# Create your models here.


class Add_vehicle(models.Model):
      vehicle_no=models.CharField(max_length=200)
      parking_area_no=models.CharField(max_length=200)
      vehicle_type=models.CharField(max_length=200)
      parking_charge=models.DecimalField(max_digits=5,decimal_places=2)
      status=models.BooleanField(default=True)
      arrival_time=models.DateTimeField(default=datetime.now)
      action=models.BooleanField(default=True)

class Category(models.Model):
      parking_area_no=models.CharField(max_length=200)
      vehicle_type=models.CharField(max_length=100)
      vehicle_limit=models.CharField(max_length=200)
      parking_charge=models.DecimalField(max_digits=5,decimal_places=2)
      status = models.BooleanField(default=True)
      arrival_time=models.DateTimeField(default=datetime.now)
      action = models.BooleanField(default=True)





