from django.urls import path
from django.conf.urls import url
from . import views

from .views import employee_home, employee_profile, personality_page, find_job, createSkill, createExperience

import employee

urlpatterns = [

    path('employee-home/', employee_home, name='employee-home'),
    path('employee-profile/',
         employee_profile, name='employee-profile'),
    path('personality/', personality_page, name='personality-page'),
    path('findjob/', find_job, name='findjob'),
    path('createskill/', createSkill, name='createskill'),
    path('createexperience/', createExperience, name='createexperience'),
    # path('createskill/employee/profile',
    #    employee_profile, name='employee-profile'),


]
