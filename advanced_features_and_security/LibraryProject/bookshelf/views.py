from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm

@login_required
@permission_required('libraryapp.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'libraryapp/view_books.html', {'books': books})

@login_required
@permission_required('libraryapp.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'libraryapp/create_book.html', {'form': form})

@login_required
@permission_required('libraryapp.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'libraryapp/edit_book.html', {'form': form})

@login_required
@permission_required('libraryapp.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('view_books')
    return render(request, 'libraryapp/delete_book.html', {'book': book})

