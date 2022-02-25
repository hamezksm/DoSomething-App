from app import views 
from django.urls import path
from register import views as v

urlpatterns=[
    path('',views.welcome,name="welcome"),
    path('register/',v.register, name="register"),
    path('home/',views.home,name="home"),
]