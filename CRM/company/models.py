from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Company(models.Model):
    
    def validate_logo(self):
        if self.logo:
            if self.logo.size>102400:
                raise ValidationError('Logo size should be less than 100kb')
            
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank= True, null= True)
    email = models.EmailField(max_length=255, blank = True , null = True)
    phone = models.CharField(max_length= 255, blank = True, null= True)
    website = models.URLField(max_length=255, blank = True, null = True)
    address = models.CharField(max_length=255, blank = True, null = True)

    logo = models.ImageField(upload_to= 'company_logo', blank= True, null = True, validators=[validate_logo])
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)




    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Companies'

