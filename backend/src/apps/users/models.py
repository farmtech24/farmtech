from django.db import models
from django.contrib.auth.models import AbstractUser

class Finca(models.Model):
    """
    Model representing a finca (farm).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    """
    Custom user model representing a user of the system.
    """
    farm = models.OneToOneField(Finca, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
