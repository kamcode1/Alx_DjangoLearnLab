from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# View to handle listing all books and creating a new book
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access for unauthenticated users, full access for authenticated users
    filterset_class = BookFilter
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # Use filters.OrderingFilter and filters.SearchFilter
    search_fields = ['title', 'author']  # Fields to be searchable
    ordering_fields = ['title', 'publication_year']  # Fields to be ordered by
    ordering = ['title']  # Default ordering

# View to handle retrieving, updating, and deleting a book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows read-only access for unauthenticated users, full access for authenticated users

# View to handle creating a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allows only authenticated users to create books

# View to handle updating an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allows only authenticated users to update books

# View to handle deleting a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allows only authenticated users to delete books
