from django.shortcuts import redirect, render
from django.template.context_processors import request
from main.models import Book, Typebook

# Create your views here.

# def myBook(request):
#     return render(request, 'mydm/mydm.html')

def ChangeStatus(request):
    # เปลี่ยนข้อมูลในดาต้าเบสจากว่างเป็นไม่ว่าง---
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Book.objects.get(user_Owner_user_id=owner)
    rm = Typebook.objects.get(book_book_id = dm)
    if request.method == 'POST':
        rm.status = 'busy'
        rm.save()
        return redirect('index')
    return render(request, 'mydm/mydm.html')


def myBook(request):
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Book.objects.filter(user_Owner_user_id=owner)
    if dm:
        dm = Book.objects.get(user_Owner_user_id=owner)
        return render(request, 'mydm/mydm.html',context = {
            'dm': dm,
        })
    else:
        return redirect('Add')

    # if dm is null:
    #     return redirect('add/add.html')
    # else:
    #     return render(request, 'mydm/mydm.html',context = {
    #     'dm': dm,
    # })





# owner = user_Owner.objects.get(user_user_id=request.user)
#     dm = Book.objects.get(user_Owner_user_id=owner)
#     userr = user_customer.objects.filter(history=dm)
#     context = {
#         'userr': userr,
#     }
#     return render(request, 'checkRequest/index.html',context)
