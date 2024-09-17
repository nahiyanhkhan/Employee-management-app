from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    salary = models.FloatField()
    designation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
