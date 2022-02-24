from django.urls import path
from .import views
urlpatterns=[
    path('home',views.fnHome,name='home'),
    path('first',views.fnFirst,name='first'),
    path('contact',views.fnContact,name='contact'),
    path('login',views.fnLogin,name='login'),
    path('forgot',views.fnForgot,name='forgot'),
    path('services',views.fnServices,name='services'),
    path('reg',views.fnReg,name='reg')


]