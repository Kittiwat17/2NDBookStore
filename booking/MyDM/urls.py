
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('', views.mydormitory, name='mydormitory'),
    path('mydm/', views.mydormitory, name='mydm'),
    path('ChangeStatus/',views.ChangeStatus, name='ChangeStatus'),
]
