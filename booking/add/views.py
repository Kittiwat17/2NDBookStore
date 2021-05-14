from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.context_processors import request
from builtins import object
from main.models import Dormitory, Room, user_Owner,picture_room
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# def addDomitory(request):
#     return render(request, 'add/index.html')


@permission_required('main.add_dormitory')
@login_required
def addDomitory(request):
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Dormitory.objects.filter(user_Owner_user_id=owner)
    if not dm:
        if request.method == 'POST':
<<<<<<< Updated upstream
            name = request.POST.get('nameDM')
            typeDM = request.POST.get('typeDM')
            address = request.POST.get('address')
            maid = request.POST.get('maid')
            internet = request.POST.get('internet')
            parking = request.POST.get('parking')
            security = request.POST.get('security')
            cctv = request.POST.get('cctv')
            pictureDM = request.FILES.get('pictureDM')
            typeRoom = request.POST.get('typeRoom')
            sizeRoom = request.POST.get('sizeRoom')
            Room_price = request.POST.get('Room_price')
            pictureRoom1 = request.FILES.get('pictureRoom1')
            pictureRoom2 = request.FILES.get('pictureRoom2')
            pictureRoom3 = request.FILES.get('pictureRoom3')
            pictureRoom4 = request.FILES.get('pictureRoom4')
            pictureRoom5 = request.FILES.get('pictureRoom5')
=======
            name = request.POST.get('nameBook')
            typeb = request.POST.get('typebook')
            nameauthor = request.POST.get('authorname')
            year = request.POST.get('datey')
            lang = request.POST.get('language')
            con = request.POST.get('contact')
            detail = request.POST.get('more')
            picture_book = request.FILES.get('picturebook')
            price = request.POST.get('price')
>>>>>>> Stashed changes

            user_owner = user_Owner.objects.get(user_user_id=request.user.id)
            user_Owner_user_id = user_owner


<<<<<<< Updated upstream
            status = 'empty'
            dormitory = Dormitory(NameDM=name, typeP=typeDM, maid=maid, internet=internet, parking=parking,
                                security=security, cctv=cctv, address=address, picture=pictureDM, user_Owner_user_id=user_Owner_user_id)
            dormitory.save()

            room = Room(type_room=typeRoom, size=sizeRoom, status=status, Room_Price=Room_price,
                    dormitory_dormitory_id=dormitory )
            room.save()
            pc_room = picture_room(Room_picture1=pictureRoom1, Room_picture2=pictureRoom2, Room_picture3=pictureRoom3, Room_picture4=pictureRoom4, Room_picture5=pictureRoom5, room_room_id = room)
            pc_room.save()
=======
            # status = 'empty'
            book = Book(NameB=name, Author=nameauthor, Year=year, Language=lang, Contact=contact,
            Detail=detail, Picture=picture_book)
            book.save()
            # dormitory = Dormitory(NameDM=name, typeP=typeDM, maid=maid, internet=internet, parking=parking,
            #                     security=security, cctv=cctv, address=address, picture=pictureDM, user_Owner_user_id=user_Owner_user_id)
            # dormitory.save()
            typebook = Typebook(Type=typeb, Price=price)
            typebook.save
            # room = Room(type_room=typeRoom, size=sizeRoom, status=status, Room_Price=Room_price,
            #         dormitory_dormitory_id=dormitory )
            # room.save()
            # pc_room = picture_room(Room_picture1=pictureRoom1, Room_picture2=pictureRoom2, Room_picture3=pictureRoom3, Room_picture4=pictureRoom4, Room_picture5=pictureRoom5, room_room_id = room)
            # pc_room.save()
>>>>>>> Stashed changes
            return redirect('index')
        return render(request, template_name='add/index.html')
    else:
        return redirect('mydm')
