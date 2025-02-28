from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    credits = models.IntegerField(default=20)

class CreditRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    requested_credits = models.IntegerField()
    approved = models.BooleanField(default=False)
