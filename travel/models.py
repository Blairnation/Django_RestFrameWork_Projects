from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE )
    gender = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)
    id_num = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.user.username