
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.detail, name='detail'),
    path('<int:user_owner_user_id>',views.detail, name='detail'),
    path('Add/', views.go_to_Add, name='Add'),
    path('create_comment/<int:typebook_id>',views.create_comment, name='create_comment')

]
