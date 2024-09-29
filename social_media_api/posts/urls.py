from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router to register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)  # The 'r' indicates that 'posts' is a raw string
router.register(r'comments', CommentViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]
