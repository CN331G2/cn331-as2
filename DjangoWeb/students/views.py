from django.shortcuts import render

from .models import Student
# Create your views here.

def index(request) :
    students = Student.objects.all()
    return render(request, 'students/index.html' ,{
        'students': students
    })