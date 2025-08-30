from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class FeedView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Get posts from users the current user follows
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

