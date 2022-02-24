from django.shortcuts import render

# Create your views here.
def fnHome(request):
    return render(request,'home.html')
def fnFirst(request0):
    return render(request0,'first.html')
def fnContact(request1):
    return render(request1,'contact.html')
def fnLogin(request2):
    return render(request2,'login.html')
def fnForgot(request3):
    return render(request3,'forgot.html')
def fnServices(request4):
    return render(request4,'services.html')
def fnReg(request5):
    return render(request5,'reg.html')


