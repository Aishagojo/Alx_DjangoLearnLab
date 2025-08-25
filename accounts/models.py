from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)  # Changed from ImageField
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')
    
    def __str__(self):
        return self.username
