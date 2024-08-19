from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Using Django's built-in LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Using Django's built-in LogoutView
    path('register/', views.Registration.as_view(), name='register')  # Custom Registration view
]
