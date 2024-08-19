
from django.urls import path
from .views import list_books, LibraryDetailView, Registration  # Ensure list_books is imported
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', Registration.as_view(), name='register')
]

