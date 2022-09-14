from django.db import models

# from django.contrib.auth.models import Student

# Create your models here.

class Course(models.Model):
    c_id = models.CharField(max_length=5, unique=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    semmester = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    seat_count = models.IntegerField(default=0, null=True, blank=True)
    max_seat = models.IntegerField(null=True, blank=True, default=5)
    quota = models.BooleanField(default=True)
    # register = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.id} code:{self.c_id} title:{self.title} semmester:{self.semester} year:{self.year} seat count:{self.seat_count} seat max:{self.max_seat}quota:{self.quota}"

class Attendance(models.Model):
    ID = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    year = models.IntegerField()
    courses = models.ManyToManyField(Course, blank=True, related_name="attendances")

    def __str__(self):
        return f"{self.id} code:{self.ID} name:{self.name} year:{self.year}"
