from django import forms
from datetime import datetime 

class todoform(forms.Form):
    title=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder':"Enter task title"}))
    desc=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':"Enter task description"}))

    lastdate=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':"Enter Last date to complete"}))