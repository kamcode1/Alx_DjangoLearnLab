from rest_framework import status
from rest_framework import response
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import IsAuthenticated, AllowAny

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        # Custom logic here if needed
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    quertset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        # Custom logic here if needed
        serializer.save()
# Create your views here.
