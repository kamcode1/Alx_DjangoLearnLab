# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import token auth view
from .views import BookList, BookViewSet, BookListCreateAPIView  # Import your views including the new BookList

# Initialize the router
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
     # New URL pattern for the BookList view
    path('books-list/', BookList.as_view(), name='book-list'),  # Add new URL pattern for the BookList view
   
    # Existing URL for the old view
    path('api/books-old/', BookListCreateAPIView.as_view(), name='book_list_create_view'),
    
    # Include URLs managed by the router for the new BookViewSet
    path('api/', include(router.urls)),

   
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
