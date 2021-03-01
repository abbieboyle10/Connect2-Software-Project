from django.urls import path
from django.conf.urls import url
from . import views

from .views import employer_home, employer_profile, jobs, browse, createJob

import employer

urlpatterns = [

    path('employer-home/', employer_home, name='employer-home'),
    path('employer-profile/', employer_profile, name='employer-profile'),
    path('jobs/', jobs, name='jobs'),
    path('browse/', browse, name='browse'),
    path('createjob/', createJob, name='createjob'),



]
