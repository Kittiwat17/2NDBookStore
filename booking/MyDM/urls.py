
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('', views.mydormitory, name='mydormitory'),
    path('mydm/', views.myBook, name='mydm'),
    path('mydm/delete', views.deleteBook, name='delete'),
    # path('ChangeStatus/',views.ChangeStatus, name='ChangeStatus'),
]
