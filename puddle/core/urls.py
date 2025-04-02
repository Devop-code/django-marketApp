from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as  auth_views
from . import views
from .form import LoginForm
app_name = 'core'
urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path("login/",auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm),name="login")
  ]
