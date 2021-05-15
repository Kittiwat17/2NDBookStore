from django.shortcuts import render
from main.models import user_Owner, Book, Typebook,user_owner_user_customer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from urllib import request
from gc import get_objects
from builtins import object

# Create your views here.

# def detail(request):
#     return render(request, 'detail/detail.html')



def detail(request, user_owner_user_id):
    rm = Typebook.objects.get(book_book_id=user_owner_user_id)
    dm = Book.objects.get(id=user_owner_user_id)
    mas = user_owner_user_customer.objects.filter(typebook_id=rm.id)
    # pc = picture_typebook.objects.get(typebook_typebook_id=rm)
    return render(request,'detail/detail.html',context={
        'rm':rm,
        'dm':dm,
        'mas': mas,
        # 'pc':pc
    })
def go_to_Add(request):
    return render(request, 'add/index.html')


def create_comment(request, typebook_id):
    typebook = Typebook.objects.get(id=typebook_id)
    if request.POST:
        text = request.POST.get('comment')
        mes = user_owner_user_customer.objects.create(
            message=text,
            typebook_id=typebook,
            create_by=request.user,
        )
        return redirect('detail', typebook.book_book_id.id)
    return redirect('detail', typebook.book_book_id.id)