from django import forms
from django.forms  import ModelForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        




        


		