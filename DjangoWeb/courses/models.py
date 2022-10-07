from email.policy import default
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    c_id = models.CharField(max_length=5, unique=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    semmester = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    seat_count = models.IntegerField(default=0, null=True, blank=True)
    max_seat = models.IntegerField(null=True, blank=True, default=5)
    quota = models.BooleanField(default=True)
    attend = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"code:{self.c_id} seat count:{self.seat_count} seat max:{self.max_seat} quota:{self.quota}"

    def is_seat_available(self):
        return self.attend.count() < self.max_seat