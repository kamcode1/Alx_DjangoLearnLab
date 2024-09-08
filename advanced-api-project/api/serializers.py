from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.Serializer):
    """
    Serialaizer for the Book model. Includes validation to ensure
    the publication year is not in the future.
    """
    
    class Meta:
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the fututre.")
        return value

class AuthorSerializer(serializers.Serializer):
    """
    Serializer for the Author model. Includes a nested BookSerializer
    to represent related books.
    """

    books = BookSerializer(many=True, read_only=True)
    class Meta:
        fields = ['name', 'books']
