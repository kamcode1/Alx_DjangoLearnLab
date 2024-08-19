from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Book
from django.contrib import messages
from .models import Library  
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.views import View

def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class Register(CreateView):
    form_class  = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'relationship_app/register.html'

class CustomLoginView(View):
    template_name = 'relationship_app/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect('list_books')  # Redirect to some view after login
            else:
                messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {'form': form})


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to login page after logout