from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}

class User(AbstractUser):
    username = None
    email = models.CharField(max_length=50,unique=True)
    phone = models.CharField(max_length=14, **NULLABLE)
    country = models.CharField(max_length=50, **NULLABLE)
    avatar = models.ImageField(upload_to='media/')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []