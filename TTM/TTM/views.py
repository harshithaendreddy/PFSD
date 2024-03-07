from django.shortcuts import render


def homePage(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def registrationPage(request):
    return render(request,"register.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")
def adminhome(request):
    return render(request,"adminhome.html")