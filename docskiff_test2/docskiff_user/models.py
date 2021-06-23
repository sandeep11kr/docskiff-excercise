from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_fruit = models.CharField(max_length=20,
                                      blank=True,
                                      null=True)
