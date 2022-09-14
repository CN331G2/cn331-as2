from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path("<str:c_id>", views.course, name="course"),
    path("<int:c_id>/book", views.book, name="book"),
]