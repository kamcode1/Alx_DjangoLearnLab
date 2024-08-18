import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Query 1: Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)

# Sample Query 2: List all books in a library
def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(book.title)

# Sample Query 3: Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

# Running the sample queries
if __name__ == "__main__":
    query_books_by_author('Author Name')
    query_books_in_library('Library Name')
    query_librarian_for_library('Library Name')
