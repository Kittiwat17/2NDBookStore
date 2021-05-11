from django.shortcuts import render
from main.models import user_Owner, Dormitory, Room, user_owner_user_customer, picture_room
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from urllib import request
from gc import get_objects
from builtins import object

# Create your views here.

# def detail(request):
#     return render(request, 'detail/detail.html')



def detail(request, user_owner_user_id):
    rm = Room.objects.get(dormitory_dormitory_id=user_owner_user_id)
    dm = Dormitory.objects.get(id=user_owner_user_id)
    mas = user_owner_user_customer.objects.filter(room_id=rm.id)
    pc = picture_room.objects.get(room_room_id=rm)
    return render(request,'detail/detail.html',context={
        'rm':rm,
        'dm':dm,
        'mas': mas,
        'pc':pc
    })
def go_to_Add(request):
    return render(request, 'add/index.html')


def create_comment(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.POST:
        text = request.POST.get('comment')
        mes = user_owner_user_customer.objects.create(
            message=text,
            room_id=room,
            create_by=request.user,
        )
        return redirect('detail', room.dormitory_dormitory_id.id)
    return redirect('detail', room.dormitory_dormitory_id.id)