from django.shortcuts import render
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# Create your views here.


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer




class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception =True)
        user = serializer.validated_data['user']

        token = RefreshToken.for_user(user)
        access_token = str(token.access_token)
        refresh_token = str(token)


        return Response(
            {
                'username': user.username,
                'email': user.email,
                'company': user.company,
                'role': user.role,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 
            status = status.HTTP_200_OK
        )
    
    

