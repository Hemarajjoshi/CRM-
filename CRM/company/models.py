from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank= True, null= True)
    email = models.EmailField(max_length=255, blank = True , null = True)
    phone = models.CharField(max_length= 255, blank = True, null= True)
    website = models.URLField(max_length=255, blank = True, null = True)
    address = models.CharField(max_length=255, blank = True, null = True)

    logo = models.ImageField(upload_to= 'company_logo', blank= True, null = True)
    created_at = models.DateField(auto_now_add= True)
    updated_at = models.DateField(auto_now= True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Companies'

