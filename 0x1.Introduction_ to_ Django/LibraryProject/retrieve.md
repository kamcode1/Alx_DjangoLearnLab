## Retrieve Book

### Python Command
```python
from bookshelf.models import Book

# Retrieve the book with ID 1
book = Book.objects.get(id=1)

# Display all attributes of the book
print(book.title)          # Output: 1984
print(book.author)         # Output: George Orwell
print(book.publication_year)  # Output: 1949
