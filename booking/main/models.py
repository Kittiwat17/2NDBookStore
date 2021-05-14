
from email.policy import default
from enum import Enum
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

class user_Owner(models.Model):
    user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
class Book(models.Model):
    NameB = models.CharField(max_length=255, default='')
    # ยังขาด typebook
    Author = models.CharField(max_length=255, default='')
    Year = models.CharField(max_length=255, default='')
    Language = models.CharField(max_length=255, default='')
    Contact = models.TextField(max_length=255)
    Detail = models.CharField(max_length=255, default='')
    Picture = models.ImageField(default='')
# class Book(models.Model):
#     TYPE = (
#         ('female', 'female'),
#         ('male', 'male'),
#     )
#     typeP = models.CharField(choices=TYPE, max_length=255, default='found')
#     NameDM = models.CharField(max_length=255, default='')
#     maid = models.BooleanField(null=True)
#     internet = models.BooleanField(null=True)
#     parking = models.BooleanField(null=True)
#     security = models.BooleanField(null=True)
#     cctv = models.BooleanField(null=True)
#     address = models.TextField(max_length=50)
#     picture = models.ImageField(default='')
#     user_Owner_user_id = models.ForeignKey(user_Owner, on_delete=models.CASCADE)   

class Typebook(models.Model):
    # empty = 'empty'
    # full = 'full'
    Cartoon = 'cartoon'
    Fiction = 'fiction'
    Documentary = 'documentary'
    Fairy = 'fairy'
    # Air = 'Air'
    # Fan = 'Fan'
    # Typetypebook = (
    #     (Air, 'Air'),
    #     (Fan, 'Fan'),
    # )
    # type_room = models.CharField(
    #     max_length=50,
    #     choices=TypeRoom,
    #     default='',
    # )
    Size = (
        (Cartoon, 'cartoon'),
        (Fiction, 'fiction'),
        (Documentary, 'documentary'),
        (Fairy, 'fairy')
    )
    # size = models.CharField(
    #     max_length=50,
    #     choices=Size,
    #     default='',
    # )
    # Status = (
    #     (empty, 'empty'),
    #     (full, 'full'),
    # )
    # status = models.CharField(
    #     max_length=50,
    #     choices=Status,
    #     default='',
    # )
    # Room_Price = models.IntegerField(null=True)
    book_book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=True)    
    

# class user_customer(models.Model):
#     user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
#     romm_room_id = models.ForeignKey(typebook, on_delete=models.CASCADE ,null=True)
#     history = models.ForeignKey(Book ,on_delete=models.CASCADE,null=True)
#     Send_request = models.BooleanField(default=False)

    #start_time = models.DateTimeField(auto_now=True)
    #end_time = models.DateTimeField(auto_now=True)


# class Furniture(models.Model):
#     List_furniture = models.TextField(max_length=50,null=True)
#     romm_typebook_id = models.ForeignKey(typebook, on_delete=models.CASCADE,null=True)

# class Booking(models.Model):
#     start_time = models.DateTimeField(auto_now=True)
#     end_time = models.DateTimeField(auto_now=True)
#     date = models.DateTimeField(auto_now=True)
#     user_customer_user_id = models.ForeignKey(
#         user_customer, on_delete=models.CASCADE)
#     typebook_typebook_id = models.ForeignKey(typebook, on_delete=models.CASCADE)
# comment
# class user_owner_user_customer(models.Model):
#     message = models.TextField(max_length=50,null=True)
#     typebook_id = models.ForeignKey(typebook, on_delete=models.CASCADE)
#     create_date = models.DateTimeField(auto_now=True)
#     create_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return "message in post:"+self.message

# class picture_typebook(models.Model):
#     typebook_picture1 = models.ImageField(default='',null=True)
#     typebook_picture2 = models.ImageField(default='',null=True)
#     typebook_picture3 = models.ImageField(default='',null=True)
#     typebook_picture4 = models.ImageField(default='',null=True)
#     typebook_picture5 = models.ImageField(default='',null=True)
#     typebook_typebook_id = models.ForeignKey(typebook, on_delete=models.CASCADE)