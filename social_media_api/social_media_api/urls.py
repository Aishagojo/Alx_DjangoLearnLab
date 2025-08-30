from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts app endpoints: register, login, profile, follow/unfollow
    path('api/accounts/', include('accounts.urls')),
    
    # Posts app endpoints: posts CRUD and feed
    path('api/posts/', include('posts.urls')),
]

