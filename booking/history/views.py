# dm = id for domitory
from builtins import object

from django.shortcuts import render
from django.template.context_processors import request

from main.models import user_customer , user_Owner,Dormitory,Room

# Create your views here.


def History(request):
    userr = user_customer.objects.get(user_user_id=request.user)
    dm = Dormitory.objects.get(pk=int(userr.history.id))
    rms = Room.objects.get(dormitory_dormitory_id=dm)
    return render(request, 'history/index.html',context = {
         'rm': rms,
         'dm': dm,
         'userr': userr,
    })

def update_history(request, user_owner_id):
    dm = Dormitory.objects.get(id=user_owner_id)
    rm = Room.objects.get(dormitory_dormitory_id=dm.id)
    if request.method == 'POST':
        print(request.user.id)
        user_cus = user_customer.objects.get(user_user_id=request.user)
        user_cus.history = dm
        user_cus.save()
    return render(request,'history/index.html', context={
        'dm':dm,
        'rm':rm
    })
    
