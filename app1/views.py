from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable":"the variable that is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')

def contact(request):
    if request.method=="POST":
        emailid=request.POST.get('emailid')
        address=request.POST.get('address')
        query=request.POST.get('query')
        name=request.POST.get('name')
        contact=Contact(emailid=emailid,address=address,query=query,name=name,date=datetime.today())
        contact.save()
        messages.success(request,"Submitted Successfully!")
    return render(request,'contact.html')

def egg_menu(request):
    return render(request,'egg_menu.html')

def bbq_menu(request):
    return render(request,'barbeque_menu.html')

def pizza_menu(request):
    return render(request,'pizza_menu.html')

def desserts(request):
    return render(request,'desserts_menu.html')

def toast_menu(request):
    return render(request,'toast_menu.html')

def pasta_menu(request):
    return render(request,'pasta_menu.html')

def locations(request):
    return render(request,'location.html')

def delivery(request):
    return render(request,'delivery.html')