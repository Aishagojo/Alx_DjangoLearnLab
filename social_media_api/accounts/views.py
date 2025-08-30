# accounts/views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CustomUser

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if user_to_follow == request.user:
        return JsonResponse({'status': 'error', 'message': 'Cannot follow yourself'}, status=400)
    
    request.user.following.add(user_to_follow)
    return JsonResponse({'status': 'success', 'message': f'You are now following {user_to_follow.username}'})

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if user_to_unfollow == request.user:
        return JsonResponse({'status': 'error', 'message': 'Cannot unfollow yourself'}, status=400)
    
    request.user.following.remove(user_to_unfollow)
    return JsonResponse({'status': 'success', 'message': f'You have unfollowed {user_to_unfollow.username}'})

