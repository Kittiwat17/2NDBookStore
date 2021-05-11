
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    # path('', views.addDomitory, name='Add'),
    path('', views.addDomitory, name='Add'),
    # path('', views.receiveBook, name='Receive')
]
