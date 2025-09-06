from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # List all user profiles
    path('profiles/', views.user_profiles, name='user_profiles'),

    # Example Book/Library views (if you add them later)
    # path('books/', views.list_books, name='list_books'),
    # path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # path('add_book/', views.add_book, name='add_book'),
    # path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    # path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]

