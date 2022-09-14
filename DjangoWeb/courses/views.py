from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Course, Attendance

# Create your views here.

def index(request) :
    return render(request, 'courses/index.html' ,{
        'courses': Course.objects.all()
    })

def attendance(request, attendance_id):
    course = Course.objects.get(pk=course_id)
    return render(request, "courses/course.html", {
        "flight": course,
        "passengers": course.attendances.all(),
        "non_passengers": Attendance.objects.exclude(courses=course)
    })

def book(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(pk=course_id)
        attendance = Attendance.objects.get(pk=int(request.POST["attendance"]))
        attendance.courses.add(course)

        return HttpResponseRedirect(reverse("course", args=(course.id,)))