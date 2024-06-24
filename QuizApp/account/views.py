from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import Register

class context:
    user={
        "Initial":"NA",
        "uname":"NA",
        "uemail":"NA",
        "upass":"NA",
        "udob":"NA",
        "udesg":"NA",
        "ucoins":"NA",
        "uscore":"NA",
        "urank":"NA"
    }
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"signup.html")

def signup(request):

    uname=request.POST['uname']	
    uemail=request.POST['uemail']
    upass=request.POST['upass']
    udob=request.POST['udob']
    udesg=request.POST['udesg']
    ucoins=int(10)
    uscore=int(0)
    urank=int(1000)
    person=Register(uname=uname,uemail=uemail,upass=upass,udob=udob,udesg=udesg,ucoins=ucoins,uscore=uscore,urank=urank)
    person.save()

    return redirect("/register")

def login(request):
    return render(request,"login.html")

def signin(request):
    uemail=request.POST['uemail']
    upass=request.POST['upass']
    auth=Register.objects.filter(uemail=uemail,upass=upass).values()
    if not auth:
        return redirect("/")
    
    context.user["uname"]=auth[0]["uname"]
    context.user["Initial"]="NA"
    context.user["uemail"]=auth[0]["uemail"]
    context.user["upass"]=auth[0]["upass"]
    context.user["udob"]=auth[0]["udob"]
    context.user["udesg"]=auth[0]["udesg"]
    context.user["ucoins"]=auth[0]["ucoins"]
    context.user["uscore"]=auth[0]["uscore"]
    context.user["urank"]=auth[0]["urank"]
    # print(context.user)
    user=context.user

    return render(request,"home.html",{"userDetails":user})