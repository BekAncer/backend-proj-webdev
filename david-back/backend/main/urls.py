from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('vehicles/', views.VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', views.VehicleRetrieveUpdateDestroyView.as_view(), name='vehicle-detail'),
]