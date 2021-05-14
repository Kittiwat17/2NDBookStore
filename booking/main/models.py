
from email.policy import default
from enum import Enum

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

class user_Owner(models.Model):
    user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
<<<<<<< Updated upstream
=======
class Book(models.Model):
    NameB = models.CharField(max_length=255, default='')
    # ยังขาด typebook
    Author = models.CharField(max_length=255, default='')
    Year = models.CharField(max_length=255, default='')
    Language = models.CharField(max_length=255, default='')
    Contact = models.CharField(max_length=255)
    Detail = models.TextField(max_length=255, default='')
    price = models.CharField(max_length=255, default='')
    Picture = models.ImageField(default='')
>>>>>>> Stashed changes

class Dormitory(models.Model):
    TYPE = (
        ('female', 'female'),
        ('male', 'male'),
    )
    typeP = models.CharField(choices=TYPE, max_length=255, default='found')
    NameDM = models.CharField(max_length=255, default='')
    maid = models.BooleanField(null=True)
    internet = models.BooleanField(null=True)
    parking = models.BooleanField(null=True)
    security = models.BooleanField(null=True)
    cctv = models.BooleanField(null=True)
    address = models.TextField(max_length=50)
    picture = models.ImageField(default='')
    user_Owner_user_id = models.ForeignKey(user_Owner, on_delete=models.CASCADE)   

class Room(models.Model):
    empty = 'empty'
    full = 'full'
    rBIG = 'BIG'
    rMEDIUM = 'MEDIUM'
    rSMALL = 'SMALL'
    Air = 'Air'
    Fan = 'Fan'
    TypeRoom = (
        (Air, 'Air'),
        (Fan, 'Fan'),
    )
    type_room = models.CharField(
        max_length=50,
        choices=TypeRoom,
        default='',
    )
    Size = (
        (rBIG, 'BIG'),
        (rMEDIUM, 'MEDIUM'),
        (rSMALL, 'SMALL'),
    )
    size = models.CharField(
        max_length=50,
        choices=Size,
        default='',
    )
<<<<<<< Updated upstream
    Status = (
        (empty, 'empty'),
        (full, 'full'),
    )
    status = models.CharField(
        max_length=50,
        choices=Status,
        default='',
    )
    Room_Price = models.IntegerField(null=True)
    dormitory_dormitory_id = models.ForeignKey(Dormitory, on_delete=models.CASCADE,null=True)    
=======
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
>>>>>>> Stashed changes
    

class user_customer(models.Model):
    user_user_id = models.OneToOneField(User ,on_delete=models.CASCADE)
<<<<<<< Updated upstream
    romm_room_id = models.ForeignKey(Room, on_delete=models.CASCADE ,null=True)
    history = models.ForeignKey(Dormitory ,on_delete=models.CASCADE,null=True)
    Send_request = models.BooleanField(default=False)
=======
    romm_room_id = models.ForeignKey(typebook, on_delete=models.CASCADE ,null=True)
    history = models.ForeignKey(Book ,on_delete=models.CASCADE,null=True)
    Send_request = models.BooleanField(default=False)

>>>>>>> Stashed changes
    #start_time = models.DateTimeField(auto_now=True)
    #end_time = models.DateTimeField(auto_now=True)


class Furniture(models.Model):
    List_furniture = models.TextField(max_length=50,null=True)
    romm_room_id = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)

class Booking(models.Model):
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now=True)
    user_customer_user_id = models.ForeignKey(
        user_customer, on_delete=models.CASCADE)
    room_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
# comment
class user_owner_user_customer(models.Model):
    message = models.TextField(max_length=50,null=True)
<<<<<<< Updated upstream
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
=======
    typebook_id = models.ForeignKey(typebook, on_delete=models.CASCADE, null=True)
>>>>>>> Stashed changes
    create_date = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "message in post:"+self.message

class picture_room(models.Model):
    Room_picture1 = models.ImageField(default='',null=True)
    Room_picture2 = models.ImageField(default='',null=True)
    Room_picture3 = models.ImageField(default='',null=True)
    Room_picture4 = models.ImageField(default='',null=True)
    Room_picture5 = models.ImageField(default='',null=True)
    room_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)