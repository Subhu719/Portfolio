from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexpage(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')

    context = {
        'portfolios': portfolios
    }   
    
    return render(request, 'index.html', context,)

def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-created_at')

    context = {
        'portfolios': portfolios
    }
    return render(request, 'portfolio-details.html', context)


#  portfolios = Portfolio.objects.all().order_by('-created_at')

#      context = {
#         'portfolios': portfolios
#      }


# category =category.objects.all()

def service(request):
    
    return render(request,'service-details.html')

def contactform(request):
    if (request.method=='POST'):
       name =request.POST.get('name')
       email =request.POST.get('email')
       subject =request.POST.get('subject')
       msg =request.POST.get('msg')
       data =contact.objects.create(
           name=name,
           email=email,
           subject=subject,
           msg=msg,
           
       )
       data.save() 
        
    return redirect('/')
