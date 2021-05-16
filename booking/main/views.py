from builtins import object
from fnmatch import filter
from main.forms import register_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.contrib.messages.api import success
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from main.models import Book, user_Owner, Typebook
from django.db.models import Q

# Create your views here.

# def index(request):
#     return render(request, 'main/index.html')


# def login(request):
#     return render(request, 'main/login.html')

def auth_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = "Username or Password Incorrect!!"
            context['username'] = username
            context['password'] = password
            context['error'] = "Username or Password Incorrect!!"
            return render(request, 'main/login.html', context)
        pass
    else:
        return render(request, 'main/login.html')


def auth_logout(request):
    logout(request)
    return redirect('index')


def index(request):
    search_name = ''
    search_gender = ''
    # search_maid = None
    # search_internet = None
    # search_parking = None
    # search_security = None
    # search_cctv = None
    # search_air_or_fan = None
    # search_size = None
    if request.POST:
        search_name = request.POST.get('name')
        search_gender = request.POST.get('gender')
        # if search_gender == 'select':
        #     search_gender = 'male'
        search_maid = request.POST.get('maid')
        # search_maid = covertTF(search_maid)
        search_internet = request.POST.get('internet')
        # search_internet = covertTF(search_internet)
        search_parking = request.POST.get('parking')
        # search_parking = covertTF(search_parking)
        search_security = request.POST.get('security')
        # search_security = covertTF(search_security)
        search_cctv = request.POST.get('cctv')
        
        # search_cctv = covertTF(search_cctv)
        # ad = ad.filter(Q(NameDM__contains=search_name) , Q(typeP=search_gender) , Q(maid=convert1(search_maid)) , Q(internet=convert1(search_internet)) , Q(parking=convert1(search_parking)) , Q(security=convert1(search_security)), Q(cctv=convert1(search_cctv)))

        ad = Book.objects.all()
        ad = ad.filter(NameDM__icontains=search_name)
        ad = ad.filter(typeP__icontains=search_gender)
        ad = ad.filter(maid=bool(int(search_maid)))
        ad = ad.filter(internet=bool(int(search_internet)))
        ad = ad.filter(parking=bool(int(search_parking)))
        ad = ad.filter(security=bool(int(search_security)))
        ad = ad.filter(cctv=bool(int(search_cctv)))
        # ad = ad.filter(NameDM__icontains=search_name , typeP__icontains=search_gender , maid=bool(search_maid), internet=bool(search_internet) , parking=bool(search_parking) , security=bool(search_security), cctv=bool(search_cctv))
        

    else:
        ad = Book.objects.all()
        tp = Typebook.objects.all()
    
        # if request.POST.get('maid') != 'select':
        #     ad = ad.filter
        # if request.POST.get('internet') != 'select':
        #     ad = ad.filter
        
    context = { 
        'ad': ad,
        'tp': tp
    }

    return render(request, 'main/index.html', context=context)

# def covertTF(x):
#     if x=='select':
#         return None
#     else:
#         return x
# def convert1(x):
#     if x == 'True':
#         return True
#     if x == 'False':
#         return False
#     return x
    


def register(request):
    context = {}
    errors = ''
    if request.method == 'POST':
        userr = register_form(request.POST)
        password2 = request.POST.get('password2')
        password = request.POST.get('password')
        if password == password2:
            
            if userr.is_valid():
                userr = userr.save()
                userr.set_password(userr.password)
                userr.save()
                if request.POST.get('roll') == 'customer':
                    group = Group.objects.get(name='User')
                    userr.groups.add(group)
                    customer = user_customer()
                    customer.user_user_id = userr
                    customer.save()
                if request.POST.get('roll') == 'owner':
                    group = Group.objects.get(name='Owner')
                    userr.groups.add(group)
                    owner = user_Owner()
                    owner.user_user_id = userr
                    owner.save()
                return redirect('login')
        else:
            errors = 'รหัสผ่านไม่ตรงกัน'
    else:
        userr = register_form()
    return render(request, 'register.html', context={
        'form': userr,
        'errors': errors
        })



    # if request.POST:
    #     username = request.POST.get('username')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     email = request.POST.get('email')
    #     if password1 != password2:
    #         context['error'] = 'รหัสผ่านไม่ตรงกัน'
    #         return redirect('register')
    #     else:
    #         user = User.objects.create_user(
    #             username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
    #         user.save()
    #         if request.POST.get('roll') == 'customer':
    #             group = Group.objects.get(name='User')
    #             user.groups.add(group)
    #             customer = user_customer()
    #             customer.user_user_id = user
    #             customer.save()
    #         if request.POST.get('roll') == 'owner':
    #             group = Group.objects.get(name='Owner')
    #             user.groups.add(group)
    #             owner = user_Owner()
    #             owner.user_user_id = user
    #             owner.save()
    #         return redirect('login')
    # return render(request, 'register.html')
