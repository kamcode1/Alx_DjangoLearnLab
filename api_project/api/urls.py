# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListCreateAPIView  # Import your existing views

# Initialize the router
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # Include URLs for the existing views
    path('api/books-old/', BookListCreateAPIView.as_view(), name='book_list_create_view'),
    
    # Include URLs managed by the router for the new BookViewSet
    path('api/', include(router.urls)),
]
