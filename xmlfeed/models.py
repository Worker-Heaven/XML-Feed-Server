from django.db import models

class SITES(models.Model):
    url = models.CharField(max_length=250)
    items_list = models.CharField(max_length=250)

class CAR_INFO(models.Model):
    site = models.ForeignKey(SITES, on_delete=models.CASCADE)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Samll'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)