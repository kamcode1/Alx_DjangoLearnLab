# blog/urls.py

from django.urls import path
from .views import (
    register, login_view, logout_view, profile,  # Authentication views
    PostListView, PostDetailView, PostCreateView,  # CRUD views for Post model
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),

    # Blog Post CRUD URLs
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]

