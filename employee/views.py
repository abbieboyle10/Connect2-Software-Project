from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from account.decorators import employee_required, employee_check
from account.models import Employee, Skill, Job
from .forms import SkillForm, ExperienceForm
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(employee_check, login_url='employer-home')
def employee_home(request,):
    user = request.user

    context = {
        'user': user,


    }
    return render(request, 'employee/employee-home.html', context)
    # return HttpResponse('Hello world')


@login_required(login_url='login')
@user_passes_test(employee_check, login_url='employer-profile')
def employee_profile(request):

    employee = Employee.objects.get(user=request.user)
    skills = employee.skill_set.all()
    experiences = employee.experience_set.all()
    context = {
        'employee': employee,
        'skills': skills,
        'experiences': experiences,

    }

    return render(request, 'employee/profile.html', context)


@user_passes_test(employee_check, login_url='jobs')
def personality_page(request):

    return render(request, 'employee/personality.html')


@user_passes_test(employee_check, login_url='jobs')
def find_job(request):
    jobs = Job.objects.all()

    context = {'jobs': jobs}
    return render(request, 'employee/findjob.html', context)


def createSkill(request):
    form = SkillForm()
    employee = Employee.objects.get(user=request.user)
    skills = employee.skill_set.all()
    experiences = employee.experience_set.all()
    context = {'employee': employee, 'skills': skills,
               'experiences': experiences, }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'employee/profile.html', context)

    context = {'form': form}
    return render(request, 'employee/skills_form.html', context)


def createExperience(request):
    form = ExperienceForm()
    employee = Employee.objects.get(user=request.user)
    experiences = employee.experience_set.all()
    skills = employee.skill_set.all()
    context = {'employee': employee,
               'experiences': experiences, 'skills': skills, }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'employee/profile.html', context)

    context = {'form': form}
    return render(request, 'employee/experiences_form.html', context)
