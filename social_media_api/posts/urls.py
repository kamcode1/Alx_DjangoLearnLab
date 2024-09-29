from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', user_feed, name='user_feed'),  # User feed
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    path('posts/<int:post_id>/unlike/', unlike_post, name='unlike_post'),
]
