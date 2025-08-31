from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serialized_posts = [
            {"id": p.id, "author": p.author.username, "content": p.content, "created_at": p.created_at}
            for p in posts
        ]
        return Response(serialized_posts)

