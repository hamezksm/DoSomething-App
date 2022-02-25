from django.shortcuts import render

# Create your views here.

#takes you to the get started page
def welcome(request):

    return render(request,'main/welcome.html')


#takes you to the home page
def home(request):
    
    return render(request,'main/home.html')