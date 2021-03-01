from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
# Create your views here.
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView
from account.forms import EmployeeSignUpForm, EmployerSignUpForm, EmployeeModelForm, EmployerModelForm
from .models import *

# Create your views here.
from django.http import HttpResponse


def Register(request):

    return render(request, 'account/register.html')


def SingUp(request):

    return render(request, 'reg.html')


def Reg_Employee(request):
    if request.user.is_authenticated:
        return redirect('home-view')
    else:
        form = EmployeeSignUpForm()
        if request.method == 'POST':
            form = EmployeeSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'account/employeereg.html', context)


def Reg_Employer(request):
    if request.user.is_authenticated:
        return redirect('employee-home')
    else:
        form = EmployerSignUpForm()
        if request.method == 'POST':
            form = EmployerSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'account/employerreg.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('employee-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('employee-home')

            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
