from django.urls import path
from .views import FeedView, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

# Feed endpoint
urlpatterns += [
    path('feed/', FeedView.as_view(), name='feed'),
]

