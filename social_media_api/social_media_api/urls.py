from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts app endpoints: follow/unfollow
    path('', include('accounts.urls')),  # URLs like /follow/<int:user_id>/ and /unfollow/<int:user_id>/

    # Posts app endpoints: feed
    path('', include('posts.urls')),     # URL like /feed/
]

