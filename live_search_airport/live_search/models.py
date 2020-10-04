from django.db import models


class Airport(models.Model):
    iata = models.CharField(max_length=4)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return f'{self.iata} - {self.city}'
