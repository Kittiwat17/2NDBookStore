
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.check, name='checkRequest'),
    path('request/',views.requestdm, name='requestdm'),
    path('accept/<int:user_id>',views.acceptrequest, name='acceptrequset'),
    # path('', views.sendrequest, name='sendrequest'),
]
