"""Users models"""


#Django
from django.db import models
from django.contrib.auth.models import AbstractUser

"user models"
class users(AbstractUser):
    
    phone_number = models.CharField(max_length=20,blank=True)
    
    email = models.EmailField(blank=True,unique=True)
    
    biography = models.CharField(max_length=200,blank=True)
    
    photo = models.ImageField(upload_to="user/pictures",blank=True, null = True)

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.username


# Create your models here.


