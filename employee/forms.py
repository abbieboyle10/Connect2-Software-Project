from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from account.models import *


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
