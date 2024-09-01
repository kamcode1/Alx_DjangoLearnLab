# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Your existing view
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

# New ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for creating, retrieving, updating, and deleting books.
    """
    queryset = Book.objects.all()  # Define the queryset to be used for CRUD operations
    serializer_class = BookSerializer  # Specify the serializer to use
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
