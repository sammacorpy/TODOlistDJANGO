from django import forms
from datetime import datetime 

class DateInput(forms.DateInput):
    input_type = 'date'

class todoform(forms.Form):
    title=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':"Enter task title"}))
    desc=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':"Enter task description"}))

    lastdate=forms.DateField(widget=DateInput)