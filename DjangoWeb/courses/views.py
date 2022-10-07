from ssl import AlertDescription
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Course

# Create your views here.

def index(request) :
    return render(request, 'courses/index.html' ,{
        'courses': Course.objects.all().order_by('c_id')
    })

def course(request, id):
    course = Course.objects.get(pk=id)
    User = get_user_model()
    users = User.objects.all()
    course.seat_count = course.attend.count()
    if course.max_seat <= course.seat_count:
        course.quota = False
    course.save()
    return render(request, "courses/course.html", {
        "course": course,
        "User" : users
    })

def book(request, id):
    course = Course.objects.get(pk=id)
    if course.quota == True :
        course.attend.add(request.user)
        course.seat_count = course.attend.count()
        if course.seat_count == course.max_seat:
            course.quota = False
        course.save()
    return HttpResponseRedirect(reverse('quota'))