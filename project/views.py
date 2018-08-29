from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
#from .models import Community_post
#from .forms import Community_PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import Signup_form, Login_form
from django.contrib.auth import login, authenticate


def index(request):
    if request.user.is_authenticated:
        return render(request, 'project/home.html', {})
    elif request.user.is_anonymous:
        #return render(request, 'project/login.html', {})
        return Login(request)

def Login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'project/home.html', {})
        else:
            return HttpResponse('로그인 실패')
    else:
        form = Login_form()
        return render(request, 'project/login.html', {'form': form})

def signup(request):
    if request.user.is_annoymous:
        render(request, 'project/signup.html', {})

    