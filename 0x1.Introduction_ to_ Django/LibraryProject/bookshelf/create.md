# Creating a Book Instance

To create a `Book` instance with the title "1984", author "George Orwell", and publication year 1949, use the following command in the Django shell:

```python
# First, start the Django shell
python manage.py shell

# Then, run the following commands inside the shell
from bookshelf.models import Book

# Create the Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify the creation
book  # Expected output: <Book: 1984 by George Orwell (1949)>
