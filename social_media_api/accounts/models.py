# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Optional bio field
    bio = models.TextField(blank=True)

    # Profile picture – allow blank and null to avoid migration issues
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Self-referential ManyToMany for following
    following = models.ManyToManyField(
        'self',               # points to the same model
        symmetrical=False,    # following is directional
        related_name='followers',  # reverse accessor to get all followers
        blank=True            # allow empty following list
    )

    def __str__(self):
        return self.username

