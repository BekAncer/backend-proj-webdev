from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView, status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserSerializer, VehicleSerializer
from .models import CustomUser, Vehicle
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(APIView):
    def post(self, request):
        print(CustomUser.objects.all())
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehicleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehicleListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, carbody):
        vehicles = Vehicle.objects.filter(carbody=carbody)
        if vehicles:
            serializer = VehicleSerializer(vehicles, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No vehicles found with the specified carbody."}, status=status.HTTP_404_NOT_FOUND)
        