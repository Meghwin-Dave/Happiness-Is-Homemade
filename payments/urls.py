from django.urls import path
from .views import *
 
urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
]