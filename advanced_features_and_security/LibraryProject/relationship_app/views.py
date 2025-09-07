from django.shortcuts import render, get_object_or_404
from .models import RelationshipProfile  # ✅ Match models.py

def index(request):
    return render(request, "relationship_app/index.html")

def profile_list(request):
    profiles = RelationshipProfile.objects.all()
    return render(request, "relationship_app/profile_list.html", {"profiles": profiles})

def profile_detail(request, pk):
    profile = get_object_or_404(RelationshipProfile, pk=pk)
    return render(request, "relationship_app/profile_detail.html", {"profile": profile})

