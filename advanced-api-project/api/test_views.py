from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='Author 1')

        # Create a book
        self.book = Book.objects.create(
            title='Book 1',
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')  # Make sure the name matches your url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_create_book(self):
        url = reverse('book-create')  # Make sure the name matches your url
        data = {
            'title': 'Book 2',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Book 2')

    def test_update_book(self):
        url = reverse('book-update', args=[self.book.id])  # Make sure name matches
        data = {
            'title': 'Book 1 Updated',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Book 1 Updated')

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.id])  # Make sure name matches
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

