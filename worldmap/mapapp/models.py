from django.db import models

class Reservoir(models.Model):
    name = models.CharField(max_length=200, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
