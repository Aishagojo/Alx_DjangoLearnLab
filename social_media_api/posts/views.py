# posts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def feed(request):
    following_users = request.user.following.all()  # Get all users current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

