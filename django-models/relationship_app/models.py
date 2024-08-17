from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.
class Author(models.Model):
    name = CharField(max_length=100)

class Book(models.Model):
    title = CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)