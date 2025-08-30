# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    # One self-referential ManyToMany for following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',  # This creates the reverse accessor
        blank=True
    )

