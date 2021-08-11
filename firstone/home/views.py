from django.db.models.base import Model
from django.shortcuts import render,HttpResponse
from datetime import datetime

from django.views.generic.detail import DetailView
from home.models import Contact, Services
from django.contrib import messages
from django.views.generic import ListView,DeleteView

# Create your views here.

def index(request):
    # return HttpResponse('this is home page')
    
   
    return render(request, "new1.html",{'Link':'http://127.0.0.1:8000/services'})


def about(request):

    

    return render(request, "about.html",{'Link':'http://127.0.0.1:8000/contact'})
    # return HttpResponse('this is about page')    

class services(ListView):
    Model = Services
    template_name = 'services.html'


    def get_queryset(self):
        
        return Services.objects.order_by('id')
    # return render(ListView, "services.html" )

    # return HttpResponse('this is services page')  


class detail(DetailView):
    Model = Services
    template_name = 'detail.html'

    def get_queryset(self):
        
        return Services.objects.order_by('id')




    

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name') 
        email= request.POST.get('email') 
        phone= request.POST.get('phone') 
        desc= request.POST.get('desc')
        contact=  Contact(name=name, email=email, phone=phone,desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'We have received your info, we will contact you soon!')


   
    return render(request, "contact.html")
    # return HttpResponse('this is contact page')     
