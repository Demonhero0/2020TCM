from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=12)
    number = models.IntegerField(default=0)

class Disease(models.Model):
    name = models.CharField(max_length=12)
    introduction = models.TextField(default="")
    symptom = models.TextField(default="")
    treatment = models.TextField(default="")
    medicines = models.TextField(default="")
    

    def __str__(self):
        return self.name

# Create your models here.
