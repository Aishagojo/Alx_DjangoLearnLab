from django.contrib import admin
from .models import RelationshipProfile  # ✅ Match models.py

@admin.register(RelationshipProfile)
class RelationshipProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "website")

