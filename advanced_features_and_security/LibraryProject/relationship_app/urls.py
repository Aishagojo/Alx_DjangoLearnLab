# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage for this app
    path('profiles/', views.profile_list, name='profile_list'),  # Example: list profiles
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),  # Example: profile detail
]

