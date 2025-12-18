from django.shortcuts import render
from userapp.serializers import *
from userapp.models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


# class UserRegisterView(APIView):

#     permission_classes = [AllowAny]

#     def post(self, request):

#         user_serialzer = Userserializer(data = request.data)

#         if user_serialzer.is_valid():

#             user=user_serialzer.save()

#             return Response(user_serialzer.data,status=status.HTTP_201_CREATED)
        
#         return Response(user_serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):

#     authentication_classes = [BasicAuthentication]

#     permission_classes = [IsAuthenticated]

#     def post(self,request):

#         user = request.user

#         refresh = RefreshToken.for_user(user) #usernmae password user_id
        
#         return Response(
#             {
#                 "message":"login success",
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh)
#             },
#             status=status.HTTP_200_OK
#         )


# class ProductListCreateView(ListCreateAPIView):

#     queryset = ProductModel.objects.all()

#     serializer_class = Productserializer

#     permission_classes=[IsAuthenticated]

#     authentication_classes = [JWTAuthentication]

#     def perform_create(self,serializer):

#         serializer.save(user = self.request.user)
