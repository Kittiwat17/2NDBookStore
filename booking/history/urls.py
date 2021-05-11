
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('historylist/', views.History, name='historylist'),
    path('<int:user_owner_id>',views.update_history, name='history'),
]
