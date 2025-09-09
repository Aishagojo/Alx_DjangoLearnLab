from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# 1. ListAPIView (BookList) — optional, but your urls.py is still using it
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 2. ModelViewSet (BookViewSet) — for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

