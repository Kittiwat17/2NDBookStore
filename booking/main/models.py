
from email.policy import default
from enum import Enum

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

class user_Owner(models.Model):
    user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
class Book(models.Model):
    NameB = models.CharField(max_length=255, default='')
    Author = models.CharField(max_length=255, default='')
    Year = models.CharField(max_length=255, default='')
    Language = models.CharField(max_length=255, default='')
    Contact = models.CharField(max_length=255)
    Price = models.CharField(max_length=255, default='')
    Detail = models.TextField(max_length=255, default='')
    Picture = models.ImageField(default='')
class Typebook(models.Model):
    Cartoon = 'cartoon'
    Fiction = 'fiction'
    Documentary = 'documentary'
    Fairy = 'fairy'
    Typee = (
        (Cartoon, 'cartoon'),
        (Fiction, 'fiction'),
        (Documentary, 'documentary'),
        (Fairy, 'fairy')
    )
    typee = models.CharField(
        max_length=50,
        choices=Typee,
        default='',
    )
    book_book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=True)    
    

class user_customer(models.Model):
    user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
    romm_room_id = models.ForeignKey(Typebook, on_delete=models.CASCADE ,null=True)
    history = models.ForeignKey(Book ,on_delete=models.CASCADE,null=True)
    Send_request = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)


# class Furniture(models.Model):
#     List_furniture = models.TextField(max_length=50,null=True)
#     romm_room_id = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)

# class Booking(models.Model):
#     start_time = models.DateTimeField(auto_now=True)
#     end_time = models.DateTimeField(auto_now=True)
#     date = models.DateTimeField(auto_now=True)
#     user_customer_user_id = models.ForeignKey(
#         user_customer, on_delete=models.CASCADE)
#     room_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
# comment
class user_owner_user_customer(models.Model):
    message = models.TextField(max_length=50,null=True)
    typebook_id = models.ForeignKey(Typebook, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "message in post:"+self.message

# class picture_room(models.Model):
#     Room_picture1 = models.ImageField(default='',null=True)
#     Room_picture2 = models.ImageField(default='',null=True)
#     Room_picture3 = models.ImageField(default='',null=True)
#     Room_picture4 = models.ImageField(default='',null=True)
#     Room_picture5 = models.ImageField(default='',null=True)
#     room_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)