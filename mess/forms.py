from django import forms

class DataForm(forms.Form):
    rollno=forms.IntegerField()