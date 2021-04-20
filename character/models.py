from django.db import models


class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='static')
    description = models.TextField()
    universe = models.CharField(max_length=25)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=0) 
    strength = models.IntegerField()
    speed = models.IntegerField()