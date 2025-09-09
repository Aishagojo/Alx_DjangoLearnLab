from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView from Task 1
class BookList(generics.ListAPIView):
    """
    Simple ListAPIView to list all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD ViewSet from Task 2 with permission classes from Task 3
class BookViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet to handle all CRUD operations on Book model.
    Only authenticated users can access these endpoints.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authentication required

