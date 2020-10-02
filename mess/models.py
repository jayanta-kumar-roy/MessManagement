# from django.conf import settings
from django.db import models
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=200)
    rollno = models.BigIntegerField(unique=True)

    def __str__(self):
        return str(self.rollno)

class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.BigIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):

    student = models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    food = models.ForeignKey(Food,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.student.name;