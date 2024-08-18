from django.urls import path
from .views import list_books, LibraryDetailView  # Ensure list_books is imported

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]

