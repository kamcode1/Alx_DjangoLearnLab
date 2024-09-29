from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import permissions  # Import permissions from Django REST Framework
from .models import User as CustomUser
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser here
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key})

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Make sure IsAuthenticated is used directly here
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    request.user.following.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])  # Use permissions.IsAuthenticated here as well
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)