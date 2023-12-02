from django.db import models
class Ernar(models.Model):
 name = models.CharField(max_length=255)
 price = models.IntegerField() 