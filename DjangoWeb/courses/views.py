import pkgutil
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Course, Attendance

# Create your views here.

def index(request) :
    return render(request, 'courses/index.html' ,{
        'courses': Course.objects.all()
    })

def course(request, c_id):
    course = Course.objects.get(pk=c_id)
    return render(request, "courses/course.html", {
        "course": course,
        "attendances": course.attendances.all(),
        "non_attendances": Attendance.objects.exclude(courses=course)
    })

def book(request, c_id):
    if request.method == "POST":
        course = Course.objects.get(pk=c_id)
        attendance = Attendance.objects.get(pk=int(request.POST["attendance"]))
        attendance.courses.add(course)

        return HttpResponseRedirect(reverse("course", args=(course.id,)))