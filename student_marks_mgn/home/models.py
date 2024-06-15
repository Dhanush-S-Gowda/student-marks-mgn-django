from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    std_id = models.CharField(max_length=20)
    sub1_marks = models.FloatField(default=0)
    sub2_marks = models.FloatField(default=0)
    sub3_marks = models.FloatField(default=0)
    sub4_marks = models.FloatField(default=0)
    sub5_marks = models.FloatField(default=0)
    percentage = models.FloatField(default=0)