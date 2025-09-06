from django.http import HttpResponse
from .models import UserProfile

def index(request):
    """Home page view"""
    return HttpResponse("Welcome to the Relationship App!")

def user_profiles(request):
    """List all user profiles"""
    profiles = UserProfile.objects.all()
    output = ", ".join([str(profile) for profile in profiles])
    return HttpResponse(f"User Profiles: {output}")

