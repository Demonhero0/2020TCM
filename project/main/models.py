from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=12)
    number = models.IntegerField(default=0)

class Disease(models.Model):
    name = models.CharField(max_length=12)
    introduction = models.TextField(default="")
    symptom = models.TextField(default="")
    treatment = models.TextField(default="")
    medicine = models.TextField(default="")
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=12)
    composition = models.CharField(max_length=32)
    effect = models.CharField(max_length=32)
    diseases = models.ManyToManyField(
        Disease,
        blank=True,
        related_name="medicines",
    )

    def __str__(self):
        return self.name

# Create your models here.
