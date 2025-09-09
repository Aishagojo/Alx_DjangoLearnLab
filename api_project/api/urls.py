from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Router for full CRUD endpoints
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Task 1 ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Task 2 CRUD endpoints via router
    path('', include(router.urls)),
]

