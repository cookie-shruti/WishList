from home.models import Services
from django.contrib import admin
from django.urls import path
from home import views
from .views import services,detail

urlpatterns = [
   path("", views.index, name='home'),
   path("about",views.about , name='about'),
   path("services",services.as_view(), name='services'),
   path("contact",views.contact, name='contact page'),
   path("detail/<int:pk>",detail.as_view(),name='detail'),
   

]

