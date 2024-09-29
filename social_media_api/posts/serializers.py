from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    # This will show the username of the author instead of the user's ID
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    # This will show the username of the author instead of the user's ID
    author = serializers.StringRelatedField(read_only=True)
    # Nested comments within the post
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'comments', 'created_at', 'updated_at']
