from django.contrib import admin
from django.urls import path,include
from register import views as v
from app import views as views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('register/',v.register,name="register"),
    path('',include('app.urls')),
    path('',include('django.contrib.auth.urls')),
    path('',include('feed.urls'))

]