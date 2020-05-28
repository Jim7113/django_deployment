from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from login_app.forms import userform,userinfo_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from login_app.models import UserInfo
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    dict = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        dict = {'user_basic_info' : user_basic_info , 'user_more_info' : user_more_info }

    return render(request, 'login_app/index.html', context=dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = userform(data=request.POST)
        user_info_form = userinfo_form(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()  #for password encryption
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user #for one to one relation

            if 'profile_img' in request.FILES:
                user_info.profile_img = request.FILES['profile_img'] #uploading in directory

            user_info.save()

            registered = True


    else:
        user_form = userform()
        user_info_form = userinfo_form()

    dict = {'user_form' : user_form ,
            'user_info_form' : userinfo_form ,
            'Registered' : registered }

    return render(request, 'login_app/register.html', context=dict)


def login_page(request):
    dict = {}
    return render(request, 'login_app/login.html', context=dict)


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('login_app:index'))

            else:
                return HttpResponse("Account is not active!")
        else:
            return HttpResponse("login info is wrong!")
    else:
        # return render(request, 'login_app/login.html', {})
        return HttpResponseRedirect(reverse('login_app:login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:index'))
