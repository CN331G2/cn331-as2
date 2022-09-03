from django.db import models

# Create your models here.

class Student(models.Model):
    ID = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.id} code:{self.ID} name:{self.name} year:{self.year}"