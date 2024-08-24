## Delete Book
from bookshelf.models import Book
### Python Command
```python
# Delete the book
book.delete()

# Try to retrieve all books to confirm deletion
books = Book.objects.all()
print(books)  # Output: <QuerySet []> (Empty QuerySet)
