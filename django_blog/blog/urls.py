from django.urls import path
from .views import register, login_view, logout_view, profile

urlpatterns = [
    path('register/', register, name='register'),  # URL pattern for registration
    path('login/', login_view, name='login'),  # URL pattern for login
    path('logout/', logout_view, name='logout'),  # URL pattern for logout
    path('profile/', profile, name='profile'),  # URL pattern for profile management
]
