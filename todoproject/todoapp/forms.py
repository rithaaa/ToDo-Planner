from django import forms
from django.contrib.auth.models import User
from . models import Person,Tasks

class PersonUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class PersonDetailForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['email','phone']
        
class TaskInfo(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['name','date']