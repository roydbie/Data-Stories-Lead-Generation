from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    bins = models.IntegerField()
    residents = models.IntegerField()

    def __str__(self):
        return self.name
