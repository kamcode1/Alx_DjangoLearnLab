from django.urls import path

from relationship_app import admin_view, librarian_view, member_view
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    
    # Django's built-in views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Custom views
    path('custom_login/', views.CustomLoginView.as_view(), name='custom_login'),
    path('custom_logout/', views.CustomLogoutView.as_view(), name='custom_logout'),

    # Registration view (custom)
    path('register/', views.register, name='register'),
    path('admin_dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian_dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member_dashboard/', member_view.member_dashboard, name='member_dashboard'),
]
