from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def query_books_in_library(library_name):
    # List all books in a library
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def query_librarian_for_library(library_name):
    # Retrieve the librarian for a library
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == "__main__":
    # Replace 'Author Name' and 'Library Name' with actual names from your database
    author_books = query_books_by_author('Author Name')
    print(f"Books by Author: {[book.title for book in author_books]}")

    library_books = query_books_in_library('Library Name')
    print(f"Books in Library: {[book.title for book in library_books]}")

    librarian = query_librarian_for_library('Library Name')
    print(f"Librarian for Library: {librarian.name}")
