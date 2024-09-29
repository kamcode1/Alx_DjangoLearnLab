from django.urls import path
from .views import RegisterView, LoginView, follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),  # Follow a user
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),  # Unfollow a use
]
