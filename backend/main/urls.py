from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    # path('login/', views.UserLogin.as_view(), name='user-login')
]