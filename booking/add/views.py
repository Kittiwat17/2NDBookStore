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
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Book.objects.filter(user_Owner_user_id=owner)
    if not dm:
        if request.method == 'POST':
            post = request.POST.get('typepost')
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

            book = Book(NameB=name, Author=nameauthor, Year=year, Language=lang, Contact=con,Price=price,
            Detail=detail, Picture=picture_book, user_Owner_user_id=user_Owner_user_id)
            book.save()

            typebook = Typebook(typee=typeb, select=post, book_book_id=book)
            typebook.save()
            return redirect('index')
        return render(request, template_name='add/index.html')
    else:
        return redirect('mydm')
