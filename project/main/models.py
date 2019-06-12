from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=12)
    number = models.IntegerField(default=0)

# Create your models here.
