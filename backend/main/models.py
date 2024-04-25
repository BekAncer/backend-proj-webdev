from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# class Car(models.Model):
#     car_id: models.AutoField(primary_key=True);
#     model: models.CharField(max_length=100, db_index=True);
#     price: models.DecimalField(max_digits=30, decimal_places=2);
#     description: models.TextField();
#     imageUrl: models.TextField();
#     ratingUrl: models.TextField();
