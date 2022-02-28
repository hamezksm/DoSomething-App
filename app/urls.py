from unicodedata import name
from app import views 
from django.urls import path

urlpatterns=[
    path('',views.welcome,name="welcome"),
    path('home/',views.home,name="home"),
]