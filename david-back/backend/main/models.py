from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    imageUrl = models.URLField()
    ratingUrl = models.URLField()
    carbody = models.CharField(max_length=100)

    def __str__(self):
        return self.model