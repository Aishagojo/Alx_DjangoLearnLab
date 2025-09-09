from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Model to store author information.
    Each author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model to store book information.
    Each book is linked to an author (ForeignKey).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Custom validation to ensure publication_year is not in the future
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError('Publication year cannot be in the future.')

