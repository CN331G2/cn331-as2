from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1)
    year = models.IntegerField()
    seat = models.IntegerField()
    quota = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} code:{self.code} name:{self.name} semmester:{self.semester} year:{self.year} seat:{self.seat} quota:{self.quota}"

