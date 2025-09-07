from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "extra_info")   # ✅ removed role
    list_filter = ("user",)                       # ✅ removed role

admin.site.register(UserProfile, UserProfileAdmin)

