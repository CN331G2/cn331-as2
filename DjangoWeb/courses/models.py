from django.db import models

import courses

# Create your models here.
class W_quota(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1)
    year = models.IntegerField()
    seat = models.IntegerField()
    quota = models.IntegerField(default= False)

class Course(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1)
    year = models.IntegerField()
    seat = models.IntegerField()
    quota = models.ForeignKey(W_quota, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}:{self.code}:{self.name}:{self.semester}:{self.year}:{self.seat}:{self.quota}"

