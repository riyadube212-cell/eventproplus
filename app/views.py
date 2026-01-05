from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def indexpage(request):
    banner=Banner.objects.filter(id=1)
    return render(request,'index.html',{"banner":banner})


def queryeve(request):
    print("work")
    if request.method=="POST":
        print("work2")
        try:
            # Get form data
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            event = request.POST['event']
            confirm = request.POST['confirm'] == 'on' or request.POST['confirm'] == 'true'
            
            # Validate required fields
            
            # Create the inquiry
            inquiry = EventQuery.objects.create(
                name=name,
                email=email,
                phone=phone,
                event=event,
                confirm=confirm
            )
            
            # Handle AJAX request
            
            # Handle regular form submission
            messages.success(request, 'Thank you! Your request has been submitted successfully. We will contact you soon!')
            return redirect('/')
            
        except Exception as e:
            return redirect('/')
        

    return render(request,"query.html")

def mayank(request):
    return render(request,"intro.html")
def kushi(request):
    return render(request,"khushiprofile.html")
def keshav(request):
    return render(request,"keshavindex.html")

def kshtij(request):
    return render(request,"kshtij.html")

def riya(reqeust):
    return render(reqeust,"riyaindex.html")