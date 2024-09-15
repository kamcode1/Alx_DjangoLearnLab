# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import post
from .forms import CustomUserCreationForm, UserUpdateForm, PostForm

# ------------------- Authentication Views -------------------

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Profile Update View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# ------------------- Blog Post CRUD Views -------------------

# ListView to display all blog posts
class PostListView(ListView):
    model = post
    template_name = 'blog/post_list.html'  # Template for listing posts
    context_object_name = 'posts'
    ordering = ['-published_date']  # Order posts by newest first

# DetailView to show individual blog posts
class PostDetailView(DetailView):
    model = post
    template_name = 'blog/post_detail.html'  # Template for post details

# CreateView to allow authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Template for creating/editing posts

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author to the logged-in user
        return super().form_valid(form)

# UpdateView to enable post authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Reusing the create form template

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit

# DeleteView to let authors delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirming deletion
    success_url = reverse_lazy('post-list')  # Redirect after successful deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete
