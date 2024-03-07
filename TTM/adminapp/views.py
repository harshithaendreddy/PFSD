from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Update the import statement in views.py
from .models import Admin, Register, Packages
from django.contrib import messages


# Create your views here.
def ttmhome(request):
    return render(request, "ttmhome.html")
#def loginfail(request):
#    return render(request, "loginfail.html")

def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwd = request.POST["pwd"]
        flag=Register.objects.filter(username=name,password=pwd).values()#Admin is the class defined in models.py
        if flag:  #flag is not empty
            if name=="har": #har is admin
                messages.info(request,"This is admin TTM page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is User's TTM page")
            return render(request, "ttmhome.html")
        else:
            messages.info(request, "Your credentials are incorrect")
            return render(request,"loginfail.html")


def checkRegistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request , "username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages .info(request, "email existing...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request ," usercreated...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")
def checkpackages(request):
    if request.method=="POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request,"Data inserted successfully")
    else:
        return render(request,"package.html")

    messages.info(request,"Insert the data into the table")
    return render(request,"package.html")

def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
def checkChangePassword(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        opwd=request.POST["opwd"]
        npwd=request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            return render(request,"index.html")
        else:
            messages.info(request,"Password Updated")
            return render(request,"index.html")
    else:
            return render(request,"changepassword.html")
def logout(request):
    messages.info(request,"Logout")
    return render(request,"index.html")



