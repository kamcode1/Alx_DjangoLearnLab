from django.db import models

# Create your models here below


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # Add this line to return the name of the author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Add this line to return the title of the book

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name  # Add this line to return the name of the library

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  # Add this line to return the name of the librarian
