from django.urls import path
from .views import *
urlpatterns = [
    path('signupaccount/',signupaccount,name="signupaccount"),
    path('loginaccount/',loginaccount,name="loginaccount"),
    path('logoutaccount/',logoutaccount,name="logoutaccount"),
]