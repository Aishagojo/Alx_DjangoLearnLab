from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post

@login_required
def feed(request):
    # Get users the current user is following
    following_users = request.user.following.all()
    
    # Get posts from following users, newest first
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    # Prepare JSON-friendly data
    posts_data = [
        {
            'id': post.id,
            'author': post.author.username,
            'content': post.content,
            'created_at': post.created_at.isoformat()
        }
        for post in posts
    ]
    
    return JsonResponse({'feed': posts_data})

