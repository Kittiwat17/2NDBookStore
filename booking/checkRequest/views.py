from django.shortcuts import redirect, render

from main.models import Dormitory, Room, user_customer, user_Owner

# Create your views here.

def check(request):
    # owner = user_Owner.objects.get(user_user_id=request.user)
    # dm = Dormitory.objects.get(user_Owner_user_id=owner)
    # userr = user_customer.objects.filter(history=dm)
    # if (userr == null)
    return render(request, ('checkRequest/index.html'))

def requestdm(request):
    owner = user_Owner.objects.get(user_user_id=request.user)
    dm = Dormitory.objects.filter(user_Owner_user_id=owner)
    if dm:
        dm = Dormitory.objects.get(user_Owner_user_id=owner)
        userr = user_customer.objects.filter(history=dm, Send_request=False)
        context = {
            'userr': userr,
        }
        return render(request, 'checkRequest/index.html',context)
    else:
        return redirect('Add')

def acceptrequest(request, user_id):
    userr = user_customer.objects.get(pk=user_id)
    userr.Send_request = True 
    userr.save()
    return redirect('requestdm')
# def sendrequest(request):
#     owner = user_Owner.objects.get(user_user_id=request.user)
#     dm = Dormitory.objects.get(user_Owner_user_id=owner)
#     rm = Room.objects.get(room = dm)
#     if request.method == 'POST':
#         rm.Send_request = 'True'
#         rm.save()
#     return redirect('checkRequest/index.html')
