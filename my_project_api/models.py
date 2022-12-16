from django.db import models

# Create your models here.
class Countries(models.Model):
    capital = models.CharField(max_length=100)
    largest_city = models.CharField(max_length=100)
    official_languages = models.CharField(max_length=100)
    area_total = models.CharField(max_length=100)
    population = models.CharField(max_length=10)
    GDP_nominal = models.CharField(max_length=10)
