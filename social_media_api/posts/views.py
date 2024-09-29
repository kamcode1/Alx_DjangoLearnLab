from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Posts:
    - List, Create, Retrieve, Update, Destroy
    """
    queryset = Post.objects.all().order_by('-created_at')  # Order posts by creation date (newest first)
    serializer_class = PostSerializer  # Use the PostSerializer for all Post operations
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    # Override the create method to ensure the current user is set as the post's author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Comments:
    - List, Create, Retrieve, Update, Destroy
    """
    queryset = Comment.objects.all().order_by('-created_at')  # Order comments by creation date (newest first)
    serializer_class = CommentSerializer  # Use the CommentSerializer for all Comment operations
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    # Override the create method to ensure the current user is set as the comment's author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    """
    A view to generate the feed for the current user based on the posts from users they are following.
    """
    # Get all posts from the users the current user is following
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
