# from ssl import _PasswordType

# Username: Matthew
# Password: citadel1955

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class SitePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # null=True, unique=True
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'userinfo')
    name  = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('sitepassword-detail', kwargs={'pk': self.pk})