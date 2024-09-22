from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, email, password):
#         if not email:
#             raise ValueError("Email is required")
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password) 
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password):
#         user = self.create_user(email=email, password=password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
    
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)



    # login username & password OR email & password ?
