from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.context_processors import request
from builtins import object
from main.models import Book, Typebook, user_Owner
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# def addDomitory(request):
#     return render(request, 'add/index.html')


@permission_required('main.add_dormitory')
@login_required
def addDomitory(request):
    # rm = user_Owner.objects.get(user_user_id=request.user)
    # dm = Book.objects.get(book_user_id=rm)
    owner = user_Owner.objects.get(user_user_id=request.user)
    print(owner)
    dm = Book.objects.filter(user_Owner_user_id=owner)
    if not dm:
        if request.method == 'POST':
            post = request.PoST.get('typepost')
            name = request.POST.get('nameBook')
            typeb = request.POST.get('typebook')
            nameauthor = request.POST.get('authorname')
            year = request.POST.get('datey')
            lang = request.POST.get('language')
            con = request.POST.get('contact')
            price = request.POST.get('Price')
            detail = request.POST.get('more')
            picture_book = request.FILES.get('picturebook')
            

            user_owner = user_Owner.objects.get(user_user_id=request.user.id)
            user_Owner_user_id = user_owner


            # status = 'empty'
            book = Book(NameB=name, Author=nameauthor, Year=year, Language=lang, Contact=con,
            Detail=detail, Picture=picture_book)
            book.save()
            # dormitory = Dormitory(NameDM=name, typeP=typeDM, maid=maid, internet=internet, parking=parking,
            #                     security=security, cctv=cctv, address=address, picture=pictureDM, user_Owner_user_id=user_Owner_user_id)
            # dormitory.save()
            typebook = Typebook(typee=typeb, select=post)
            typebook.save
            # room = Room(type_room=typeRoom, size=sizeRoom, status=status, Room_Price=Room_price,
            #         dormitory_dormitory_id=dormitory )
            # room.save()
            # pc_room = picture_room(Room_picture1=pictureRoom1, Room_picture2=pictureRoom2, Room_picture3=pictureRoom3, Room_picture4=pictureRoom4, Room_picture5=pictureRoom5, room_room_id = room)
            # pc_room.save()
            return redirect('index')
        return render(request, template_name='add/index.html')
    else:
        return redirect('mydm')
