from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.contrib.auth import get_user_model

from courses.models import Course


# Create your views here.


def index(request):
    c = {}
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'students/index.html', c)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'students/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'students/login.html', {
        'message': 'Logged out'
    })

def quota(request):
    
    course = Course.objects.all()
    User = get_user_model()
    users = User.objects.all()
    return render(request, "students/quota.html", {
        "course": course,
        "User" : users
    })