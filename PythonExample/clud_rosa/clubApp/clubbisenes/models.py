from django.db import models


class Regions(models.Model):
    region = models.CharField(max_length=30 )
    index = models.IntegerField(default= 64)