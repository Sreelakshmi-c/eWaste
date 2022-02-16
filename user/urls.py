from django.urls import path
from .import views
urlpatterns=[
    path('',views.fnHome,name='home'),
    path('first',views.fnFirst,name='first')
]