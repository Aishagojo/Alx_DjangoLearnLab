from django.db import models
from bookshelf.models import CustomUser   # ✅ import your CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="+"   # disables reverse relation
    )
    extra_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Relationship data for {self.user.username}"

