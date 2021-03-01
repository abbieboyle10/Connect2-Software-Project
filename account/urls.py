from django.urls import path
from django.conf.urls import url
from . import views
from .views import SingUp, Reg_Employee, Reg_Employer, Register
import account

urlpatterns = [
    path('register/', Register, name='register'),
    path('singup/', SingUp, name='singup'),
    path('regemployee/', Reg_Employee, name='reg-employee'),
    path('regemployer/', Reg_Employer, name='reg-employer'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),







]
