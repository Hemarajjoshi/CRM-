from django.db import models
from invitations.models import Invitation as BaseInvitation 
from users.models import User

# Create your models here.

class Invitation(BaseInvitation):

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('lead', 'Lead'),
        ('member', 'Member')
        ]

    email = models.EmailField(max_length =100)
    invited_by = models.ForeignKey(User , on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=100)

    def __str__(self):
        return f'{self.email} was invited by {self.invited_by}'
    



