from django.db import models
from django.conf import settings

class RelationshipProfile(models.Model):  # ✅ Consistent name
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="relationship_profile"
    )
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

