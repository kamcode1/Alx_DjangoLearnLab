# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView 

# Your existing view
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
class BookList(generics.ListAPIView):
    """
    API view to retrieve list of books.
    """
    queryset = Book.objects.all()  # Define the queryset to retrieve all Book instances
    serializer_class = BookSerializer  # Define the serializer to convert Book instances to JSON
# New ViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for creating, retrieving, updating, and deleting books.
    """
    queryset = Book.objects.all()  # Define the queryset to be used for CRUD operations
    serializer_class = BookSerializer  # Specify the serializer to use
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
