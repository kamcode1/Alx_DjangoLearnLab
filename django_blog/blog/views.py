# blog/views.py


from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from taggit.models import Tag

from .models import Post, Comment
from .forms import CustomUserCreationForm, UserUpdateForm, PostForm, CommentForm

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
    model = Post
    template_name = 'blog/post_list.html'  # Template for listing posts
    context_object_name = 'posts'
    ordering = ['-published_date']  # Order posts by newest first

# DetailView to show individual blog posts
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for post details

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use self.get_object() to ensure the object is retrieved properly
        post = self.get_object()
        #Add comments related to the post
        context['comments'] = post.comments.all()
        # Add a blank form for adding a comment
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        return context



# CreateView to allow authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # Template for creating/editing posts

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author to the logged-in user
        return super().form_valid(form)

# UpdateView to enable post authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
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
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirming deletion
    success_url = reverse_lazy('post-list')  # Redirect after successful deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # Assuming you have this template

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])  # Set the post related to the comment
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  # Redirect back to the post detail page after the comment is submitted
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        post = self.get_object().post
        return reverse_lazy('post-detail', kwargs={'pk': post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_by_tag.html'  # Template to display posts by tag
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        # Get the tag based on the slug from the URL
        tag = get_object_or_404(Tag, slug=tag_slug)
        # Filter posts that have the specified tag
        return Post.objects.filter(tags__in=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the tag to the context for display purposes
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return context
       
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |  # Search in post title
                Q(content__icontains=query) |  # Search in post content
                Q(tags__name__icontains=query)  # Search in post tags
            ).distinct()  # Ensure we don't get duplicate posts
        return Post.objects.all()