from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    number_of_phone = models.CharField(max_length=15)
    delivery_address = models.CharField(max_length=200, blank=True)