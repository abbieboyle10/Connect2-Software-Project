from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from account.models import User, Employee, Employer


class EmployeeSignUpForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    county = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.first_name = self.cleaned_data.get('first_name')
        employee.last_name = self.cleaned_data.get('last_name')
        employee.county = self.cleaned_data.get('county')
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.email = self.cleaned_data.get('email')
        employee.save()

        return user


class EmployerSignUpForm(UserCreationForm):
    company_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_employer = True
        user.save()
        employer = Employer.objects.create(user=user)
        employer.email = self.cleaned_data.get('email')
        employer.company_name = self.cleaned_data.get('company_name')
        employer.phone = self.cleaned_data.get('phone')
        employer.location = self.cleaned_data.get('location')
        employer.save()

        return user


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'avatar')


class EmployerModelForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'location', 'phone')
