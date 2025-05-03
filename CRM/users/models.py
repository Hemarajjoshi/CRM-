from django.db import models
from django.contrib.auth.models import AbstractUser
from company.models import Company

# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('lead', 'Lead'),
        ('member', 'Member')
        ]
    
    email = models.EmailField(unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    role = models.CharField(max_length = 20 , choices = ROLE_CHOICES)
    company  = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)




