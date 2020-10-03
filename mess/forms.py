from django import forms
from django.forms import ModelForm
from .models import Order,Student

class DataForm(forms.Form):
    rollno=forms.IntegerField()

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields = ['name','rollno']
