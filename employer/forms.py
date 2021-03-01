from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from account.models import *


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
