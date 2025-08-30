# accounts/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow != request.user:
        request.user.following.add(user_to_follow)  # Assuming a ManyToMany 'following' field
    return redirect('profile', user_id=user_id)  # Redirect to the user's profile or any page

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow != request.user:
        request.user.following.remove(user_to_unfollow)
    return redirect('profile', user_id=user_id)

