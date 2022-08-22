from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import Contactform



def homepage(request):
    return render(request,'core/home.html')
def aboutpage(request):
    return render(request,'core/about2.html')
def gallerypage(request):
    return render(request,'core/gallery.html')
def contactpage(request):
    if request.method == 'POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Phone=request.POST['phone']
        Message=request.POST['message']
        us2=Contactform(name=Name,email=Email,phone=Phone,message=Message)
        us2.save()
        messages.success(request,'Send Successfully!!')
        return HttpResponseRedirect('/core/contact/')
    else:    
        return render(request,'core/contact.html')            

# Create your views here.
