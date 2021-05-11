from django.shortcuts import redirect, render
from django.template.context_processors import request
from main.models import Dormitory, Room, user_customer, user_Owner

# Create your views here.

# def mydormitory(request):
#     return render(request, 'mydm/mydm.html')

def ChangeStatus(request):
    # เปลี่ยนข้อมูลในดาต้าเบสจากว่างเป็นไม่ว่าง---
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Dormitory.objects.get(user_Owner_user_id=owner)
    rm = Room.objects.get(dormitory_dormitory_id = dm)
    if request.method == 'POST':
        rm.status = 'busy'
        rm.save()
        return redirect('index')
    return render(request, 'mydm/mydm.html')


def mydormitory(request):
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Dormitory.objects.filter(user_Owner_user_id=owner)
    if dm:
        dm = Dormitory.objects.get(user_Owner_user_id=owner)
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
#     dm = Dormitory.objects.get(user_Owner_user_id=owner)
#     userr = user_customer.objects.filter(history=dm)
#     context = {
#         'userr': userr,
#     }
#     return render(request, 'checkRequest/index.html',context)
