from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=120)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']
    
    def __str__(self):
        return f"{self.id} {self.email}"

