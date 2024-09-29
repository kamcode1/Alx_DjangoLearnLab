from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from notifications.models import Notification
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # Create a notification for the post's author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )
        return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()
        return Response({'message': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)