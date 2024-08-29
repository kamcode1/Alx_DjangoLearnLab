#from django.shortcuts import render
# edited the import statement
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from .models import Book

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer