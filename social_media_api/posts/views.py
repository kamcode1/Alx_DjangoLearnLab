from rest_framework import viewsets, permissions
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
