"""Definiuje wzorce adresów URL dla aplikacji USERS."""

from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    #strona logowania.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    path('logout/', views.logout_view, name='logout'),
    #Strona rejestracji.
    path('register/', views.register, name='register'),
]
