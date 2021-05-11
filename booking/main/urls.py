
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
    path('', views.index, name='index'),
    path('login/register/', views.register, name='register'),
]