# views.py
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from .permissions import IsOwner
from .serializers import UserSerializer, UserLoginSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'success':'CSRF Cookie Set'})

@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'isAuthenticated': True})
        else:
            return Response({'isAuthenticated': False})

@method_decorator(csrf_protect, name='dispatch')
class UserCreateView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

@method_decorator(csrf_protect, name='dispatch')
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner, IsAuthenticated]

class AuthenticatedUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = []
    def post(self, request, format=None):          
            serializer = UserLoginSerializer(data=request.data)
            if(serializer.is_valid()):
                username = serializer.validated_data["username"]
                password = serializer.validated_data["password"]
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return JsonResponse(serializer.errors)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
