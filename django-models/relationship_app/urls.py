from django.urls import path
from .views import list_books, LibraryDetailView, Registration, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Custom logout view
    path('register/', Registration.as_view(), name='register')  # Registration view
]
